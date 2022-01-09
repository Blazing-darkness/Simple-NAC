#Installation


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



