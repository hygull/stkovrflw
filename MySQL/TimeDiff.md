	C:\Users\rishi>mysql -u rishikesh67 -p
	Enter password: ***************
	Welcome to the MySQL monitor.  Commands end with ; or \g.
	Your MySQL connection id is 9
	Server version: 8.0.11 MySQL Community Server - GPL

	Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

	Oracle is a registered trademark of Oracle Corporation and/or its
	affiliates. Other names may be trademarks of their respective
	owners.

	Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

	mysql> show databases;
	+--------------------+
	| Database           |
	+--------------------+
	| information_schema |
	| mysql              |
	| performance_schema |
	| sys                |
	+--------------------+
	4 rows in set (0.15 sec)

	mysql> create database trial_db;
	Query OK, 1 row affected (0.11 sec)

	mysql> use trial_db;
	Database changed
	mysql> create table projects_tbl(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, project_name VARCHAR(50) NOT NULL, time_in TIME NOT NULL, time_out TIME NOT NULL);
	Query OK, 0 rows affected (0.71 sec)

	mysql> DESCRIBE project_tbl;
	ERROR 1146 (42S02): Table 'trial_db.project_tbl' doesn't exist
	mysql> DESCRIBE projects_tbl;
	+--------------+-------------+------+-----+---------+----------------+
	| Field        | Type        | Null | Key | Default | Extra          |
	+--------------+-------------+------+-----+---------+----------------+
	| id           | int(11)     | NO   | PRI | NULL    | auto_increment |
	| project_name | varchar(50) | NO   |     | NULL    |                |
	| time_in      | time        | NO   |     | NULL    |                |
	| time_out     | time        | NO   |     | NULL    |                |
	+--------------+-------------+------+-----+---------+----------------+
	4 rows in set (0.01 sec)

	mysql>
	mysql> INSERT INTO projects_tbl('SriRam Finance', '09:30', '18:45');
	ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''SriRam Finance', '09:30', '18:45')' at line 1
	mysql> INSERT INTO projects_tbl(project_name, time_in, time_out) VALUES('SriRam Finance', '09:30', '18:45');
	Query OK, 1 row affected (0.18 sec)

	mysql> SELECT * FROM projects_tbl;
	+----+----------------+----------+----------+
	| id | project_name   | time_in  | time_out |
	+----+----------------+----------+----------+
	|  1 | SriRam Finance | 09:30:00 | 18:45:00 |
	+----+----------------+----------+----------+
	1 row in set (0.00 sec)

	mysql> INSERT INTO projects_tbl(project_name, time_in, time_out) VALUES('SriRam Finance', '08:30', '18:30');
	Query OK, 1 row affected (0.12 sec)

	mysql> INSERT INTO projects_tbl(project_name, time_in, time_out) VALUES('QuantsWord', '08:00', '18:45');
	Query OK, 1 row affected (0.10 sec)

	mysql> INSERT INTO projects_tbl(project_name, time_in, time_out) VALUES('Branbox', '08:30', '18:45');
	Query OK, 1 row affected (0.11 sec)

	mysql> INSERT INTO projects_tbl(project_name, time_in, time_out) VALUES('SamTab', '08:40', '18:45');
	Query OK, 1 row affected (0.11 sec)

	mysql> INSERT INTO projects_tbl(project_name, time_in, time_out) VALUES('EdgoGage', '08:00', '18:40');
	Query OK, 1 row affected (0.10 sec)

	mysql> INSERT INTO projects_tbl(project_name, time_in, time_out) VALUES('SamTab', '08:20', '18:45');
	Query OK, 1 row affected (0.04 sec)

	mysql> INSERT INTO projects_tbl(project_name, time_in, time_out) VALUES('QuantsWord', '08:00', '18:10');
	Query OK, 1 row affected (0.10 sec)

	mysql> INSERT INTO projects_tbl(project_name, time_in, time_out) VALUES('Branbox', '08:40', '18:40');
	Query OK, 1 row affected (0.21 sec)

	mysql> INSERT INTO projects_tbl(project_name, time_in, time_out) VALUES('QuantsWord', '08:00', '19:40');
	Query OK, 1 row affected (0.08 sec)

	mysql> INSERT INTO projects_tbl(project_name, time_in, time_out) VALUES('Branbox', '08:40', '18:50');
	Query OK, 1 row affected (0.05 sec)

	mysql> SELECT * FROM projects_tbl;
	+----+----------------+----------+----------+
	| id | project_name   | time_in  | time_out |
	+----+----------------+----------+----------+
	|  1 | SriRam Finance | 09:30:00 | 18:45:00 |
	|  2 | SriRam Finance | 08:30:00 | 18:30:00 |
	|  3 | QuantsWord     | 08:00:00 | 18:45:00 |
	|  4 | Branbox        | 08:30:00 | 18:45:00 |
	|  5 | SamTab         | 08:40:00 | 18:45:00 |
	|  6 | EdgoGage       | 08:00:00 | 18:40:00 |
	|  7 | SamTab         | 08:20:00 | 18:45:00 |
	|  8 | QuantsWord     | 08:00:00 | 18:10:00 |
	|  9 | Branbox        | 08:40:00 | 18:40:00 |
	| 10 | QuantsWord     | 08:00:00 | 19:40:00 |
	| 11 | Branbox        | 08:40:00 | 18:50:00 |
	+----+----------------+----------+----------+
	11 rows in set (0.00 sec)

	mysql> SELECT TIMEDIFF(time_out, time_in) AS time_diff from projects_tbl;
	+-----------+
	| time_diff |
	+-----------+
	| 09:15:00  |
	| 10:00:00  |
	| 10:45:00  |
	| 10:15:00  |
	| 10:05:00  |
	| 10:40:00  |
	| 10:25:00  |
	| 10:10:00  |
	| 10:00:00  |
	| 11:40:00  |
	| 10:10:00  |
	+-----------+
	11 rows in set (0.01 sec)

	mysql> SELECT project_name, TIMEDIFF(time_out, time_in) AS time_diff from projects_tbl;
	+----------------+-----------+
	| project_name   | time_diff |
	+----------------+-----------+
	| SriRam Finance | 09:15:00  |
	| SriRam Finance | 10:00:00  |
	| QuantsWord     | 10:45:00  |
	| Branbox        | 10:15:00  |
	| SamTab         | 10:05:00  |
	| EdgoGage       | 10:40:00  |
	| SamTab         | 10:25:00  |
	| QuantsWord     | 10:10:00  |
	| Branbox        | 10:00:00  |
	| QuantsWord     | 11:40:00  |
	| Branbox        | 10:10:00  |
	+----------------+-----------+
	11 rows in set (0.00 sec)

	mysql>
	mysql> SELECT tbl.project_name, SEC_TO_TIME(SUM(TIME_TO_SEC(tbl.time_out) - TIME_TO_SEC(tbl.time_in))) AS time_diff from projects_tbl AS tbl GROUP BY tbl.project_name;
	+----------------+-----------+
	| project_name   | time_diff |
	+----------------+-----------+
	| SriRam Finance | 19:15:00  |
	| QuantsWord     | 32:35:00  |
	| Branbox        | 30:25:00  |
	| SamTab         | 20:30:00  |
	| EdgoGage       | 10:40:00  |
	+----------------+-----------+
	5 rows in set (0.00 sec)


	C:\Users\rishi>mysql -u rishikesh67 -p
	Enter password: ***************
	Welcome to the MySQL monitor.  Commands end with ; or \g.
	Your MySQL connection id is 10
	Server version: 8.0.11 MySQL Community Server - GPL

	Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

	Oracle is a registered trademark of Oracle Corporation and/or its
	affiliates. Other names may be trademarks of their respective
	owners.

	Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

	mysql> use projects_tbl
	ERROR 1049 (42000): Unknown database 'projects_tbl'
	mysql> use trial_db;
	Database changed
	mysql> SHOW TABLES;
	+--------------------+
	| Tables_in_trial_db |
	+--------------------+
	| projects_tbl       |
	+--------------------+
	1 row in set (0.06 sec)

	mysql> SELECT * FROM projects_tbl;
	+----+----------------+----------+----------+
	| id | project_name   | time_in  | time_out |
	+----+----------------+----------+----------+
	|  1 | SriRam Finance | 09:30:00 | 18:45:00 |
	|  2 | SriRam Finance | 08:30:00 | 18:30:00 |
	|  3 | QuantsWord     | 08:00:00 | 18:45:00 |
	|  4 | Branbox        | 08:30:00 | 18:45:00 |
	|  5 | SamTab         | 08:40:00 | 18:45:00 |
	|  6 | EdgoGage       | 08:00:00 | 18:40:00 |
	|  7 | SamTab         | 08:20:00 | 18:45:00 |
	|  8 | QuantsWord     | 08:00:00 | 18:10:00 |
	|  9 | Branbox        | 08:40:00 | 18:40:00 |
	| 10 | QuantsWord     | 08:00:00 | 19:40:00 |
	| 11 | Branbox        | 08:40:00 | 18:50:00 |
	+----+----------------+----------+----------+
	11 rows in set (0.00 sec)

	mysql> CREATE TABLE projects_tbl2 (id BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT, project_name VARCHAR(50) NOT NULL, entry_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, exit_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
	Query OK, 0 rows affected (0.51 sec)

	mysql> DESC projects_tbl2;
	+--------------+-------------+------+-----+-------------------+-----------------------------+
	| Field        | Type        | Null | Key | Default           | Extra                       |
	+--------------+-------------+------+-----+-------------------+-----------------------------+
	| id           | bigint(20)  | NO   | PRI | NULL              | auto_increment              |
	| project_name | varchar(50) | NO   |     | NULL              |                             |
	| entry_at     | datetime    | NO   |     | CURRENT_TIMESTAMP |                             |
	| exit_at      | datetime    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
	+--------------+-------------+------+-----+-------------------+-----------------------------+
	4 rows in set (0.00 sec)

	mysql> INSERT INTO `projects_tbl2`(`project_name`) VALUES('QuantsWord');
	Query OK, 1 row affected (0.14 sec)

	mysql> INSERT INTO `projects_tbl2`(project_name) VALUES('QuantsWord');
	Query OK, 1 row affected (0.10 sec)

	mysql> INSERT INTO projects_tbl2(project_name) VALUES('QuantsWord');
	Query OK, 1 row affected (0.08 sec)

	mysql> SELECT * FROM projects_tbl2;
	+----+--------------+---------------------+---------------------+
	| id | project_name | entry_at            | exit_at             |
	+----+--------------+---------------------+---------------------+
	|  1 | QuantsWord   | 2018-06-17 15:48:23 | 2018-06-17 15:48:23 |
	|  2 | QuantsWord   | 2018-06-17 15:48:33 | 2018-06-17 15:48:33 |
	|  3 | QuantsWord   | 2018-06-17 15:48:41 | 2018-06-17 15:48:41 |
	+----+--------------+---------------------+---------------------+
	3 rows in set (0.00 sec)

	mysql> UPDATE projects_tbl2 SET project_name='Branbox' WHERE id=2;
	Query OK, 1 row affected (0.12 sec)
	Rows matched: 1  Changed: 1  Warnings: 0

	mysql> SELECT * FROM projects_tbl2;
	+----+--------------+---------------------+---------------------+
	| id | project_name | entry_at            | exit_at             |
	+----+--------------+---------------------+---------------------+
	|  1 | QuantsWord   | 2018-06-17 15:48:23 | 2018-06-17 15:48:23 |
	|  2 | Branbox      | 2018-06-17 15:48:33 | 2018-06-17 15:49:47 |
	|  3 | QuantsWord   | 2018-06-17 15:48:41 | 2018-06-17 15:48:41 |
	+----+--------------+---------------------+---------------------+
	3 rows in set (0.00 sec)

	mysql> UPDATE projects_tbl2 SET project_name='SamTab' WHERE id=1;
	Query OK, 1 row affected (0.03 sec)
	Rows matched: 1  Changed: 1  Warnings: 0

	mysql> SELECT * FROM projects_tbl2;
	+----+--------------+---------------------+---------------------+
	| id | project_name | entry_at            | exit_at             |
	+----+--------------+---------------------+---------------------+
	|  1 | SamTab       | 2018-06-17 15:48:23 | 2018-06-17 15:50:55 |
	|  2 | Branbox      | 2018-06-17 15:48:33 | 2018-06-17 15:49:47 |
	|  3 | QuantsWord   | 2018-06-17 15:48:41 | 2018-06-17 15:48:41 |
	+----+--------------+---------------------+---------------------+
	3 rows in set (0.00 sec)

	mysql> INSERT INTO projects_tbl2(project_name) VALUES('EdgoGage');
	Query OK, 1 row affected (0.07 sec)

	mysql> INSERT INTO projects_tbl2(project_name) VALUES('QuantsWord');
	Query OK, 1 row affected (0.09 sec)

	mysql> INSERT INTO projects_tbl2(project_name) VALUES('Branbox');
	Query OK, 1 row affected (0.06 sec)

	mysql> SELECT * FROM projects_tbl2;
	+----+--------------+---------------------+---------------------+
	| id | project_name | entry_at            | exit_at             |
	+----+--------------+---------------------+---------------------+
	|  1 | SamTab       | 2018-06-17 15:48:23 | 2018-06-17 15:50:55 |
	|  2 | Branbox      | 2018-06-17 15:48:33 | 2018-06-17 15:49:47 |
	|  3 | QuantsWord   | 2018-06-17 15:48:41 | 2018-06-17 15:48:41 |
	|  4 | EdgoGage     | 2018-06-17 15:53:05 | 2018-06-17 15:53:05 |
	|  5 | QuantsWord   | 2018-06-17 15:53:14 | 2018-06-17 15:53:14 |
	|  6 | Branbox      | 2018-06-17 15:53:35 | 2018-06-17 15:53:35 |
	+----+--------------+---------------------+---------------------+
	6 rows in set (0.00 sec)

	mysql> UPDATE projects_tbl2 SET project_name='SamTab' WHERE id=1;
	Query OK, 0 rows affected (0.00 sec)
	Rows matched: 1  Changed: 0  Warnings: 0

	mysql> SELECT * FROM projects_tbl2;
	+----+--------------+---------------------+---------------------+
	| id | project_name | entry_at            | exit_at             |
	+----+--------------+---------------------+---------------------+
	|  1 | SamTab       | 2018-06-17 15:48:23 | 2018-06-17 15:50:55 |
	|  2 | Branbox      | 2018-06-17 15:48:33 | 2018-06-17 15:49:47 |
	|  3 | QuantsWord   | 2018-06-17 15:48:41 | 2018-06-17 15:48:41 |
	|  4 | EdgoGage     | 2018-06-17 15:53:05 | 2018-06-17 15:53:05 |
	|  5 | QuantsWord   | 2018-06-17 15:53:14 | 2018-06-17 15:53:14 |
	|  6 | Branbox      | 2018-06-17 15:53:35 | 2018-06-17 15:53:35 |
	+----+--------------+---------------------+---------------------+
	6 rows in set (0.00 sec)

	mysql> UPDATE projects_tbl2 SET project_name='SamTab2' WHERE id=1;
	Query OK, 1 row affected (0.08 sec)
	Rows matched: 1  Changed: 1  Warnings: 0

	mysql> SELECT * FROM projects_tbl2;
	+----+--------------+---------------------+---------------------+
	| id | project_name | entry_at            | exit_at             |
	+----+--------------+---------------------+---------------------+
	|  1 | SamTab2      | 2018-06-17 15:48:23 | 2018-06-17 16:00:25 |
	|  2 | Branbox      | 2018-06-17 15:48:33 | 2018-06-17 15:49:47 |
	|  3 | QuantsWord   | 2018-06-17 15:48:41 | 2018-06-17 15:48:41 |
	|  4 | EdgoGage     | 2018-06-17 15:53:05 | 2018-06-17 15:53:05 |
	|  5 | QuantsWord   | 2018-06-17 15:53:14 | 2018-06-17 15:53:14 |
	|  6 | Branbox      | 2018-06-17 15:53:35 | 2018-06-17 15:53:35 |
	+----+--------------+---------------------+---------------------+
	6 rows in set (0.00 sec)

	mysql> UPDATE projects_tbl2 SET project_name='SamTab' WHERE id=1;
	Query OK, 1 row affected (0.08 sec)
	Rows matched: 1  Changed: 1  Warnings: 0

	mysql> SELECT * FROM projects_tbl2;
	+----+--------------+---------------------+---------------------+
	| id | project_name | entry_at            | exit_at             |
	+----+--------------+---------------------+---------------------+
	|  1 | SamTab       | 2018-06-17 15:48:23 | 2018-06-17 16:00:36 |
	|  2 | Branbox      | 2018-06-17 15:48:33 | 2018-06-17 15:49:47 |
	|  3 | QuantsWord   | 2018-06-17 15:48:41 | 2018-06-17 15:48:41 |
	|  4 | EdgoGage     | 2018-06-17 15:53:05 | 2018-06-17 15:53:05 |
	|  5 | QuantsWord   | 2018-06-17 15:53:14 | 2018-06-17 15:53:14 |
	|  6 | Branbox      | 2018-06-17 15:53:35 | 2018-06-17 15:53:35 |
	+----+--------------+---------------------+---------------------+
	6 rows in set (0.00 sec)

	mysql> UPDATE projects_tbl2 SET project_name='SamTab' WHERE id=1;
	Query OK, 0 rows affected (0.00 sec)
	Rows matched: 1  Changed: 0  Warnings: 0

	mysql> SELECT * FROM projects_tbl2;
	+----+--------------+---------------------+---------------------+
	| id | project_name | entry_at            | exit_at             |
	+----+--------------+---------------------+---------------------+
	|  1 | SamTab       | 2018-06-17 15:48:23 | 2018-06-17 16:00:36 |
	|  2 | Branbox      | 2018-06-17 15:48:33 | 2018-06-17 15:49:47 |
	|  3 | QuantsWord   | 2018-06-17 15:48:41 | 2018-06-17 15:48:41 |
	|  4 | EdgoGage     | 2018-06-17 15:53:05 | 2018-06-17 15:53:05 |
	|  5 | QuantsWord   | 2018-06-17 15:53:14 | 2018-06-17 15:53:14 |
	|  6 | Branbox      | 2018-06-17 15:53:35 | 2018-06-17 15:53:35 |
	+----+--------------+---------------------+---------------------+
	6 rows in set (0.00 sec)

	mysql> INSERT INTO projects_tbl2(project_name) VALUES('Branbox');
	Query OK, 1 row affected (0.09 sec)

	mysql> INSERT INTO projects_tbl2(project_name) VALUES('QuantsWord');
	Query OK, 1 row affected (0.12 sec)

	mysql> INSERT INTO projects_tbl2(project_name) VALUES('QuantsWord');
	Query OK, 1 row affected (0.06 sec)

	mysql> INSERT INTO projects_tbl2(project_name) VALUES('EdgoGage');
	Query OK, 1 row affected (0.08 sec)

	mysql> INSERT INTO projects_tbl2(project_name) VALUES('EdgoGage');
	Query OK, 1 row affected (0.05 sec)

	mysql> DESC projects_tbl2;
	+--------------+-------------+------+-----+-------------------+-----------------------------+
	| Field        | Type        | Null | Key | Default           | Extra                       |
	+--------------+-------------+------+-----+-------------------+-----------------------------+
	| id           | bigint(20)  | NO   | PRI | NULL              | auto_increment              |
	| project_name | varchar(50) | NO   |     | NULL              |                             |
	| entry_at     | datetime    | NO   |     | CURRENT_TIMESTAMP |                             |
	| exit_at      | datetime    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
	+--------------+-------------+------+-----+-------------------+-----------------------------+
	4 rows in set (0.02 sec)

	mysql> SELECT * FROM projects_tbl;
	+----+----------------+----------+----------+
	| id | project_name   | time_in  | time_out |
	+----+----------------+----------+----------+
	|  1 | SriRam Finance | 09:30:00 | 18:45:00 |
	|  2 | SriRam Finance | 08:30:00 | 18:30:00 |
	|  3 | QuantsWord     | 08:00:00 | 18:45:00 |
	|  4 | Branbox        | 08:30:00 | 18:45:00 |
	|  5 | SamTab         | 08:40:00 | 18:45:00 |
	|  6 | EdgoGage       | 08:00:00 | 18:40:00 |
	|  7 | SamTab         | 08:20:00 | 18:45:00 |
	|  8 | QuantsWord     | 08:00:00 | 18:10:00 |
	|  9 | Branbox        | 08:40:00 | 18:40:00 |
	| 10 | QuantsWord     | 08:00:00 | 19:40:00 |
	| 11 | Branbox        | 08:40:00 | 18:50:00 |
	+----+----------------+----------+----------+
	11 rows in set (0.00 sec)

	mysql> SELECT * FROM projects_tbl2;
	+----+--------------+---------------------+---------------------+
	| id | project_name | entry_at            | exit_at             |
	+----+--------------+---------------------+---------------------+
	|  1 | SamTab       | 2018-06-17 15:48:23 | 2018-06-17 16:00:36 |
	|  2 | Branbox      | 2018-06-17 15:48:33 | 2018-06-17 15:49:47 |
	|  3 | QuantsWord   | 2018-06-17 15:48:41 | 2018-06-17 15:48:41 |
	|  4 | EdgoGage     | 2018-06-17 15:53:05 | 2018-06-17 15:53:05 |
	|  5 | QuantsWord   | 2018-06-17 15:53:14 | 2018-06-17 15:53:14 |
	|  6 | Branbox      | 2018-06-17 15:53:35 | 2018-06-17 15:53:35 |
	|  7 | Branbox      | 2018-06-17 16:02:08 | 2018-06-17 16:02:08 |
	|  8 | QuantsWord   | 2018-06-17 16:02:14 | 2018-06-17 16:02:14 |
	|  9 | QuantsWord   | 2018-06-17 16:02:16 | 2018-06-17 16:02:16 |
	| 10 | EdgoGage     | 2018-06-17 16:02:23 | 2018-06-17 16:02:23 |
	| 11 | EdgoGage     | 2018-06-17 16:02:45 | 2018-06-17 16:02:45 |
	+----+--------------+---------------------+---------------------+
	11 rows in set (0.00 sec)

	mysql> SELECT TIMEDIFF(exit_at, entry_at) FROM projects_tbl2;
	+-----------------------------+
	| TIMEDIFF(exit_at, entry_at) |
	+-----------------------------+
	| 00:12:13                    |
	| 00:01:14                    |
	| 00:00:00                    |
	| 00:00:00                    |
	| 00:00:00                    |
	| 00:00:00                    |
	| 00:00:00                    |
	| 00:00:00                    |
	| 00:00:00                    |
	| 00:00:00                    |
	| 00:00:00                    |
	+-----------------------------+
	11 rows in set (0.00 sec)

	mysql> SELECT tbl.project_name, tbl.entry_at, tbl.exit_at, SUM(TIMEDIFF(exit_at, entry_at)) as time_diff FROM projects_tbl2 as tbl;
	ERROR 1140 (42000): In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column 'trial_db.tbl.project_name'; this is incompatible with sql_mode=only_full_group_by
	mysql>
	mysql> SELECT tbl.project_name, tbl.entry_at, tbl.exit_at, SUM(TIMEDIFF(exit_at, entry_at)) as time_diff FROM projects_tbl2 as tbl GROUP BY tbl.project_name;
	ERROR 1055 (42000): Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'trial_db.tbl.entry_at' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
	mysql>
	mysql>
	mysql> SELECT tbl.project_name, SUM(TIMEDIFF(exit_at, entry_at)) as time_diff FROM projects_tbl2 as tbl GROUP BY tbl.project_name;
	+--------------+-----------+
	| project_name | time_diff |
	+--------------+-----------+
	| SamTab       |      1213 |
	| Branbox      |       114 |
	| QuantsWord   |         0 |
	| EdgoGage     |         0 |
	+--------------+-----------+
	4 rows in set (0.00 sec)

	mysql> SELECT tbl.project_name, SUM(SEC_TO_TIME(TIMEDIFF(exit_at, entry_at))) as time_diff FROM projects_tbl2 as tbl GROUP BY tbl.project_name;
	+--------------+-----------+
	| project_name | time_diff |
	+--------------+-----------+
	| SamTab       |      2013 |
	| Branbox      |       154 |
	| QuantsWord   |         0 |
	| EdgoGage     |         0 |
	+--------------+-----------+
	4 rows in set (0.00 sec)

	mysql> SELECT tbl.project_name, SUM(SEC_TO_TIME(TIMEDIFF(exit_at, entry_at))) as time_diff FROM projects_tbl2 as tbl GROUP BY tbl.project_name;
	+--------------+-----------+
	| project_name | time_diff |
	+--------------+-----------+
	| SamTab       |      2013 |
	| Branbox      |       154 |
	| QuantsWord   |         0 |
	| EdgoGage     |         0 |
	+--------------+-----------+
	4 rows in set (0.00 sec)

	mysql> SELECT TIME_TO_SEC(exit_at) FROM projects_tbl2;
	+----------------------+
	| TIME_TO_SEC(exit_at) |
	+----------------------+
	|                57636 |
	|                56987 |
	|                56921 |
	|                57185 |
	|                57194 |
	|                57215 |
	|                57728 |
	|                57734 |
	|                57736 |
	|                57743 |
	|                57765 |
	+----------------------+
	11 rows in set (0.00 sec)

	mysql> SELECT tbl.project_name, SEC_TO_TIME(SUM(TIME_TO_SEC(exit_at) - TIME_TO_SEC(entry_at))) as time_diff FROM projects_tbl2 as tbl GROUP BY tbl.project_name;
	+--------------+-----------+
	| project_name | time_diff |
	+--------------+-----------+
	| SamTab       | 00:12:13  |
	| Branbox      | 00:01:14  |
	| QuantsWord   | 00:00:00  |
	| EdgoGage     | 00:00:00  |
	+--------------+-----------+
	4 rows in set (0.00 sec)

	mysql>

