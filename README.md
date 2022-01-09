# Installation


1. Installation von FreeRadius mit SQL-Modul:

        a. sudo apt-get install freeradius freeradius-utils freeradius-sql

2. Installieren und vorbereiten der MySQL-Datenbank:

        a. sudo apt-get install mysql-server mysql-clients

        b. Anmelden mit sudo mysql –u root –p
Bei Aufforderung ein leeres Passwort eingeben.

        c. Datenbank erstellen, mit „CREATE DATABASE radius;“

        d. Neuen MySQL-Rootuser anlegen:
		CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';
		Hierbei darauf achten, dass das @-Zeichen von zwei Hochkomma umschlossen ist!!!

        e. Dem neuen MySQL-Rootuser alle Rechte geben:
		GRANT ALL PRIVILEGES ON *.* TO 'username'@'hostname';
		Auch hier wieder beim @-Zeichen darauf achten.

        f. Die neue Berechtigung anwenden:
		FLUSH PRIVILEGES;

        g. Mit „exit“ die MySQL-Datenbank verlassen und das Radius-Datenbankschema einspielen:
		sudo mysql -u root -p radius < /etc/freeradius/3.0/mods-config/sql/main/mysql/schema.sql;
		Bei Problemen überprüfen, ob auf die Datei „schema.sql“ ausreichend Zugriffsberechtigung existiert.
		Im Zweifel einfach Komplettzugriff mit chmod 777 schema.sql


3. Konfiguration von Freeradius

        a. Anpassen von „/etc/freeradius/3.0/sites-enabled/default“
		Änderungen wie folgt:

		authorize {
		#   files
		    sql
		}
		authenticate {
		}
		preacct {
		#   files
		}
		accounting {
		    sql
		}
		session {
		    sql
		}
		post-auth {
		    sql
		    Post-Auth-Type REJECT {
		    # log failed authentications in SQL, too.
		    sql
		    attr_filter.access_reject
		    }
		}


4. Zugangsdaten zum MySQL-Server eintragen 

        a. Anpassen der Datei „/etc/freeradius/3.0/mods-available/sql“:

		sql {
		    driver = "rlm_sql_mysql"
		    dialect = "mysql"
		    server = "hostname"
		    login = "username"
		    password = "userpassword"
		    radius_db = "radius"
		    #uncomment read_groups
		    read_groups = yes
		    #uncomment readclients
		    readclients = yes
}





5. Symbolischen Link setzen/anlegen:

        a. Folgenden Befehl ausführen:
		sudo ln –s /etc/freeradius/3.0/mods-available/sql /etc/freeradius/… …/3.0/mods-enabled/sql



6. Geräte in die Datenbank „radius“ einpflegen

        a. Alle Clients (Switche, WLan-Controller, etc.) welche mit Radius-server kommunizieren dürfen, in die passende Tabelle eintragen:
		INSERT INTO  nas VALUES (NULL ,  '10.0.0.254/32‘,  'Clientname', 'other', NULL ,  'Secret-Key', NULL , NULL ,  'RADIUS Client');

        b. Wichtig!!! Die MAC-Adresse des Clients muss als Username&Passwort in die Tabelle eingetragen werden:
		INSERT INTO radcheck (username, attribute, op, value) VALUES ('MAC-Adresse', 'Cleartext-Password', ':=', 'MAC-Adresse');

        c. Auch hier muss man wieder die MAC-Adresse als Name angeben.
		Gruppenname kann beliebig sein, aber identisch mit dem Gruppennamen aus dem nachfolgenden Unterpunkt ‚d.‘
		INSERT INTO radusergroup (username, groupname, priority) VALUES ('MAC-Adresse', 'Gruppenname', '1');

        d. Der Gruppenname muss identisch sein, wie bei Unterpunkt ‚c.‘.
		Der Parameter „Tunnel-Private-Group-Id“ entspricht der VLan-ID.
		INSERT INTO radgroupreply (groupname, attribute, op, value) VALUES ('Gruppenname', 'Tunnel-Type', ':=', 13), ('Gruppenname', 'Tunnel-Medium-Type', ':=', '6'), ('Gruppenname', 'Tunnel-Private-Group-Id', ':=', 100);



7. Starten und Stoppen von Freeradius:
	sudo service freeradius start/restart



