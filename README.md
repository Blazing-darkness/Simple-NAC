# Simple Network Access Control

Appliance for use of AAA in local network environments.

Main features

		Authentication:
  		802.1x
  		MAC-Auth
  		
  		Authoriziation:
		Dynamic VLan assignment
		Dynamic ACL assignment
		Dynamic QoS assignment

		Accounting:
		Logfiles & Databases

Change of Authorization (CoA) under development!

## Download

Download pre-installed appliance as OVA-file.

English version:
https://drive.google.com/file/d/17kZ0...
Password: 8z27!pQf&#+u

German version:
https://drive.google.com/file/d/1Ax5B...
Password: #8z!5pfQ%&+U

## Introduction video

https://www.youtube.com/watch?v=EzjjqeYWKGA

## Manual installation of services (Ubuntu-Server)

1. Installation of FreeRadius with SQL-modul:

        a. sudo apt-get install freeradius freeradius-utils freeradius-sql

2. Installation and preparation of MySQL-database:

        a. sudo apt-get install mysql-server mysql-clients

        b. Login with sudo mysql –u root –p
Type blank password if asked for login

        c. Create Database with „CREATE DATABASE radius;“

        d. Create new MySQL-Rootuser:
		CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';
		The @-sign should be inclosed between two exclamation marks!!!

        e. Grant all privileges to MySQL-Rootuser:
		GRANT ALL PRIVILEGES ON *.* TO 'username'@'hostname';
		Again, be aware of the @-sign.

        f. Apply new privileges:
		FLUSH PRIVILEGES;

        g. Leave MySQL-Database with "exit" and import Radius-Databasescheme:
		sudo mysql -u root -p radius < /etc/freeradius/3.0/mods-config/sql/main/mysql/schema.sql;
		Bei Problemen überprüfen, ob auf die Datei „schema.sql“ ausreichend Zugriffsberechtigung existiert.
		Im Zweifel einfach Komplettzugriff mit chmod 777 schema.sql


3. Configuration of freeradius

        a. Change of „/etc/freeradius/3.0/sites-enabled/default“
		Changes as follows:

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


4. Enter Logindata for MySQL-server

        a. Change of file „/etc/freeradius/3.0/mods-available/sql“:

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





5. Create symbolic link:

        a. Execute this command:
		sudo ln –s /etc/freeradius/3.0/mods-available/sql /etc/freeradius/… …/3.0/mods-enabled/sql



6. Insert your enddevice into database (optional). You can do this later by using the WebGUI.

        a. All clients (Switche, WLan-Controller, etc.) that are allowed to communicate with radius-server. Insert into correct table:
		INSERT INTO  nas VALUES (NULL ,  '10.0.0.254/32‘,  'Clientname', 'other', NULL ,  'Secret-Key', NULL , NULL ,  'RADIUS Client');

        b. Important!!! The MAC-Address of the client has to be entered as both, Username as well as Passwort:
		INSERT INTO radcheck (username, attribute, op, value) VALUES ('MAC-Adresse', 'Cleartext-Password', ':=', 'MAC-Adresse');

        c. Here you also have to enter MAC-Address as name:
		Gruppenname kann beliebig sein, aber identisch mit dem Gruppennamen aus dem nachfolgenden Unterpunkt ‚d.‘
		INSERT INTO radusergroup (username, groupname, priority) VALUES ('MAC-Adresse', 'Gruppenname', '1');

        d. Groupname has to be identical with point ‚c.‘ above.
		Der Parameter „Tunnel-Private-Group-Id“ entspricht der VLan-ID.
		INSERT INTO radgroupreply (groupname, attribute, op, value) VALUES ('Gruppenname', 'Tunnel-Type', ':=', 13), ('Gruppenname', 'Tunnel-Medium-Type', ':=', '6'), ('Gruppenname', 'Tunnel-Private-Group-Id', ':=', 100);


7. Installation of Python3 & Django.

Install all dependencies to use MySQL with Python:
	
		pip install mysqlclient

Eventually you also have to install this:

		sudo apt-get install python3-dev default-libmysqlclient-dev build-essential # Debian / Ubuntu
		sudo yum install python3-devel mysql-devel # Red Hat / CentOS
		
8. Finally, import the NAC-Code of this repository into Django, as a Django-App.
Finish


9. Start and Stop of freeradius.

		sudo service freeradius start/restart
	

## Switchconfiguration

Example for Cisco-IOS

		aaa new-model
		!
		aaa authentication dot1x default group radius
		aaa authorization network default group radius
		!
		aaa session-id common
		system mtu routing 1500
		!
		dot1x system-auth-control
		!
		spanning-tree mode rapid-pvst
		spanning-tree extend system-id
		!
		interface GigabitEthernet0/2
		 switchport mode access
		 authentication port-control auto
		 mab
		!
		interface Vlan1
		 ip address 10.0.0.254 255.255.255.0
		!
		interface Vlan100
		 ip address 192.168.100.254 255.255.255.0
		 ip helper-address 10.0.0.1
		!
		interface Vlan200
		 ip address 192.168.200.254 255.255.255.0
		 ip helper-address 10.0.0.1
		!
		radius server freeradius
		 address ipv4 10.0.0.1 auth-port 1812 acct-port 1813
		 key start123


Example for HP-ProCurve

		radius-server host X.X.X.X acct-port 1813 key "Kennwort"
		aaa port-access mac-based "Portnummer"  #aktivieren
		aaa port-access mac-based "Portnummer" unauth-vid "VLAN-Nummer"  #default vlan

## !!!Important notice for MAC-Authentication!!!

For MAC-AUTH you have to enter the mac of your device as user AND password!!!

Do it here: https://youtu.be/EzjjqeYWKGA?t=437

So you have to enter the MAC-Address into textfield "Username" and textfield "Value".
