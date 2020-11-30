mysql> CREATE DATABASE SQL_WORKSHEET;
Query OK, 1 row affected (0.07 sec)

mysql> USE SQL_WORKSHEET;
Database changed
mysql> CREATE TABLE games(GCode INT(3) NOT NULL PRIMARY KEY, GameName VARCHAR(20) UNIQUE, Eventcount INT(3), PrizeMoney INT(7) NOT NULL DEFAULT 10000, Dt DATE);
Query OK, 0 rows affected, 3 warnings (0.55 sec)

mysql> INSERT INTO games VALUES(101,'Carom',2,5000,'2019-01-23');
Query OK, 1 row affected (004 sec)
mysql> INSERT INTO games VALUES(102,'Badminton',2,10000,'2019-12-12');
Query OK, 1 row affected (0.07 sec)

mysql> INSERT INTO games VALUES(103,'TableTennis',4,8000,'2019-02-14');
Query OK, 1 row affected (0.06 sec)

mysql> INSERT INTO games VALUES(104,'Chess',2,9000,'2019-01-01');
Query OK, 1 row affected (0.06 sec)

mysql> INSERT INTO games VALUES(105,'LawnTennis',4,25000,'2019-03-19');
Query OK, 1 row affected (0.05 sec)

mysql> INSERT INTO games(GCode,Eventcount) VALUES(106,1);
Query OK, 1 row affected (0.05 sec)

mysql> INSERT INTO games(GCode,GameName,Eventcount,PrizeMoney) VALUES(107,'__shooting__',2,10000);
Query OK, 1 row affected (0.08 sec)

mysql> SELECT * FROM games;
+-------+--------------+------------+------------+------------+
| GCode | GameName     | Eventcount | PrizeMoney | Dt         |
+-------+--------------+------------+------------+------------+
|   101 | Carom        |          2 |       5000 | 2019-01-23 |
|   102 | Badminton    |          2 |      10000 | 2019-12-12 |
|   103 | TableTennis  |          4 |       8000 | 2019-02-14 |
|   104 | Chess        |          2 |       9000 | 2019-01-01 |
|   105 | LawnTennis   |          4 |      25000 | 2019-03-19 |
|   106 | NULL         |          1 |      10000 | NULL       |
|   107 | __shooting__ |          2 |      10000 | NULL       |
+-------+--------------+------------+------------+------------+
7 rows in set (0.00 sec)

mysql> CREATE TABLE Players(PCode INT(2) NOT NULL PRIMARY KEY, NAME VARCHAR(20) NOT NULL,GCode INT(3), FOREIGN KEY (GCode) REFERENCES games(GCode));
Query OK, 0 rows affected, 2 warnings (1.04 sec)

mysql> INSERT INTO Players VALUES(1,'Arjun',101);
Query OK, 1 row affected (0.03 sec)

mysql> INSERT INTO Players VALUES(2,'Ravi',105);
Query OK, 1 row affected (0.09 sec)

mysql> INSERT INTO Players VALUES(3,'Jignesh',101);
Query OK, 1 row affected (0.08 sec)

mysql> INSERT INTO Players VALUES(4,'Nihal',103);
Query OK, 1 row affected (0.08 sec)

mysql> INSERT INTO Players VALUES(5,'Sohail',104);
Query OK, 1 row affected (0.03 sec)

mysql> SELECT * FROM Players;
+-------+---------+-------+
| PCode | NAME    | GCode |
+-------+---------+-------+
|     1 | Arjun   |   101 |
|     2 | Ravi    |   105 |
|     3 | Jignesh |   101 |
|     4 | Nihal   |   103 |
|     5 | Sohail  |   104 |
+-------+---------+-------+
5 rows in set (0.00 sec)

mysql> SELECT GameName, PrizeMoney FROM games ORDER BY FIELD(GameName,'LawnTennis','Badminton','TableTennis','Chess','Carom');
+--------------+------------+
| GameName     | PrizeMoney |
+--------------+------------+
| NULL         |      10000 |
| __shooting__ |      10000 |
| LawnTennis   |      25000 |
| Badminton    |      10000 |
| TableTennis  |       8000 |
| Chess        |       9000 |
| Carom        |       5000 |
+--------------+------------+
7 rows in set (0.00 sec)

mysql> SELECT PCode AS PlayersCODE, NAME AS PlayersNAME FROM Players GROUP BY GCode ORDER BY GCode DESC ,NAME ASC;
+------------+------------+
| PlayersCODE | PlayersNAME |
+------------+------------+
|          2 | Ravi       |
|          5 | Sohail     |
|          4 | Nihal      |
|          1 | Arjun      |
+------------+------------+
4 rows in set (0.03 sec)

mysql> SELECT DISTINCT PrizeMoney FROM games;
+------------+
| PrizeMoney |
+------------+
|       5000 |
|      10000 |
|       8000 |
|       9000 |
|      25000 |
+------------+
5 rows in set (0.01 sec)

mysql> SELECT CHAR(PrizeMoney) FROM games;
+------------------------------------+
| CHAR(PrizeMoney)                   |
+------------------------------------+
| 0x1388                             |
| 0x2710                             |
| 0x1F40                             |
| 0x2328                             |
| 0x61A8                             |
| 0x2710                             |
| 0x2710                             |
+------------------------------------+
7 rows in set (0.00 sec)

mysql> SELECT CONCAT(GameName,' ', Dt) AS 'COMBINED' FROM games;
+------------------------+
| COMBINED               |
+------------------------+
| Carom 2019-01-23       |
| Badminton 2019-12-12   |
| TableTennis 2019-02-14 |
| Chess 2019-01-01       |
| LawnTennis 2019-03-19  |
| NULL                   |
| NULL                   |
+------------------------+
7 rows in set (0.02 sec)

mysql> SELECT LOWER(Name) FROM Players;
+-------------+
| LOWER(Name) |
+-------------+
| arjun       |
| ravi        |
| jignesh     |
| nihal       |
| sohail      |
+-------------+
5 rows in set (0.03 sec)

mysql> SELECT UPPER(GameName) FROM games;
+-----------------+
| UPPER(GameName) |
+-----------------+
| NULL            |
| __SHOOTING__    |
| BADMINTON       |
| CAROM           |
| CHESS           |
| LAWNTENNIS      |
| TABLETENNIS     |
+-----------------+
7 rows in set (0.00 sec)

mysql> SELECT TRIM(GameName) FROM games;
+----------------+
| TRIM(GameName) |
+----------------+
| NULL           |
| __shooting__   |
| Badminton      |
| Carom          |
| Chess          |
| LawnTennis     |
| TableTennis    |
+----------------+
7 rows in set (0.00 sec)

mysql> SELECT NAME,POSITION('A' IN NAME) FROM Players;
+---------+-----------------------+
| NAME    | POSITION('A' IN NAME) |
+---------+-----------------------+
| Arjun   |                     1 |
| Ravi    |                     2 |
| Jignesh |                     0 |
| Nihal   |                     4 |
| Sohail  |                     4 |
+---------+-----------------------+
5 rows in set (0.01 sec)

mysql> SELECT GameName,LENGTH(GameName) FROM games;
+--------------+------------------+
| GameName     | LENGTH(GameName) |
+--------------+------------------+
| NULL         |             NULL |
| __shooting__ |               12 |
| Badminton    |                9 |
| Carom        |                5 |
| Chess        |                5 |
| LawnTennis   |               10 |
| TableTennis  |               11 |
+--------------+------------------+
7 rows in set (0.00 sec)

mysql> SELECT Name,LEFT(Name,4) FROM Players;
+---------+--------------+
| Name    | LEFT(Name,4) |
+---------+--------------+
| Arjun   | Arju         |
| Ravi    | Ravi         |
| Jignesh | Jign         |
| Nihal   | Niha         |
| Sohail  | Soha         |
+---------+--------------+
5 rows in set (0.00 sec)

mysql> SELECT GameName,RIGHT(GameName,3) FROM games;
+--------------+-------------------+
| GameName     | RIGHT(GameName,3) |
+--------------+-------------------+
| NULL         | NULL              |
| __shooting__ | g__               |
| Badminton    | ton               |
| Carom        | rom               |
| Chess        | ess               |
| LawnTennis   | nis               |
| TableTennis  | nis               |
+--------------+-------------------+
7 rows in set (0.00 sec)

mysql> SELECT Name,MID(Name,3,5) FROM Players;
+---------+---------------+
| Name    | MID(Name,3,5) |
+---------+---------------+
| Arjun   | jun           |
| Ravi    | vi            |
| Jignesh | gnesh         |
| Nihal   | hal           |
| Sohail  | hail          |
+---------+---------------+
5 rows in set (0.00 sec)

mysql> SELECT Prizemoney,ROUND(5/100*Prizemoney,1) FROM games;
+------------+---------------------------+
| Prizemoney | ROUND(5/100*Prizemoney,1) |
+------------+---------------------------+
|       5000 |                     250.0 |
|      10000 |                     500.0 |
|       8000 |                     400.0 |
|       9000 |                     450.0 |
|      25000 |                    1250.0 |
|      10000 |                     500.0 |
|      10000 |                     500.0 |
+------------+---------------------------+
7 rows in set (0.01 sec)

mysql> SELECT Prizemoney,TRUNCATE(5/100*Prizemoney,1) FROM games;
+------------+------------------------------+
| Prizemoney | TRUNCATE(5/100*Prizemoney,1) |
+------------+------------------------------+
|       5000 |                        250.0 |
|      10000 |                        500.0 |
|       8000 |                        400.0 |
|       9000 |                        450.0 |
|      25000 |                       1250.0 |
|      10000 |                        500.0 |
|      10000 |                        500.0 |
+------------+------------------------------+
7 rows in set (0.00 sec)

mysql> SELECT MOD(PrizeMoney,Eventcount) FROM games;
+----------------------------+
| MOD(PrizeMoney,Eventcount) |
+----------------------------+
|                          0 |
|                          0 |
|                          0 |
|                          0 |
|                          0 |
|                          0 |
|                          0 |
+----------------------------+
7 rows in set (0.00 sec)

mysql> SELECT (PCode*PCode),SQRT(PCode) FROM Players;
+---------------+--------------------+
| (PCode*PCode) | SQRT(PCode)        |
+---------------+--------------------+
|             1 |                  1 |
|             9 | 1.7320508075688772 |
|            16 |                  2 |
|            25 |   2.23606797749979 |
|             4 | 1.4142135623730951 |
+---------------+--------------------+
5 rows in set (0.02 sec)

mysql> SELECT SYSDATE(),CURDATE(), NOW();
+---------------------+------------+---------------------+
| SYSDATE()           | CURDATE()  | NOW()               |
+---------------------+------------+---------------------+
| 2020-07-03 14:52:08 | 2020-07-03 | 2020-07-03 14:52:08 |
+---------------------+------------+---------------------+
1 row in set (0.00 sec)

mysql> SELECT DATE(SYSDATE());
+-----------------+
| DATE(SYSDATE()) |
+-----------------+
| 2020-07-03      |
+-----------------+
1 row in set (0.00 sec)

mysql> SELECT Dt ,DAYOFMONTH(Dt) ,MONTH(Dt) ,YEAR(Dt) ,DAYNAME(Dt) ,DAYOFWEEK(Dt) ,DAYOFYEAR(Dt) FROM games;
+------------+----------------+-----------+----------+-------------+---------------+---------------+
| Dt         | DAYOFMONTH(Dt) | MONTH(Dt) | YEAR(Dt) | DAYNAME(Dt) | DAYOFWEEK(Dt) | DAYOFYEAR(Dt) |
+------------+----------------+-----------+----------+-------------+---------------+---------------+
| 2019-01-23 |             23 |         1 |     2019 | Wednesday   |             4 |            23 |
| 2019-12-12 |             12 |        12 |     2019 | Thursday    |             5 |           346 |
| 2019-02-14 |             14 |         2 |     2019 | Thursday    |             5 |            45 |
| 2019-01-01 |              1 |         1 |     2019 | Tuesday     |             3 |             1 |
| 2019-03-19 |             19 |         3 |     2019 | Tuesday     |             3 |            78 |
| NULL       |           NULL |      NULL |     NULL | NULL        |          NULL |          NULL |
| NULL       |           NULL |      NULL |     NULL | NULL        |          NULL |          NULL |
+------------+----------------+-----------+----------+-------------+---------------+---------------+
7 rows in set (0.05 sec)

mysql> SELECT GCode,GameName,Eventcount FROM games WHERE MONTH(Dt)=1 OR MONTH(Dt)=2 OR PrizeMoney<15000;
+-------+--------------+------------+
| GCode | GameName     | Eventcount |
+-------+--------------+------------+
|   101 | Carom        |          2 |
|   102 | Badminton    |          2 |
|   103 | TableTennis  |          4 |
|   104 | Chess        |          2 |
|   106 | NULL         |          1 |
|   107 | __shooting__ |          2 |
+-------+--------------+------------+
6 rows in set (0.03 sec)

mysql> SELECT GCode,GameName FROM games WHERE GCode=101 or GCode=105;
+-------+------------+
| GCode | GameName   |
+-------+------------+
|   101 | Carom      |
|   105 | LawnTennis |
+-------+------------+
2 rows in set (0.01 sec)

mysql> SELECT GameName FROM games WHERE GameName BETWEEN "A%" AND "P%";
+------------+
| GameName   |
+------------+
| Badminton  |
| Carom      |
| Chess      |
| LawnTennis |
+------------+
4 rows in set (0.00 sec)

mysql> SELECT GameName FROM games WHERE Dt IS NULL;
+--------------+
| GameName     |
+--------------+
| NULL         |
| __shooting__ |
+--------------+
2 rows in set (0.00 sec)

mysql> SELECT COUNT(GameName) FROM games;
+-----------------+
| COUNT(GameName) |
+-----------------+
|               6 |
+-----------------+
1 row in set (0.02 sec)

mysql> SELECT COUNT(GameName) FROM games;
+-----------------+
| COUNT(GameName) |
+-----------------+
|               6 |
+-----------------+
1 row in set (0.00 sec)

mysql> SELECT SUM(Eventcount) FROM games;
+-----------------+
| SUM(Eventcount) |
+-----------------+
|              17 |
+-----------------+
1 row in set (0.00 sec)

mysql> SELECT COUNT(Dt) FROM games WHERE Eventcount > 1;
+-----------+
| COUNT(Dt) |
+-----------+
|         5 |
+-----------+
1 row in set (0.00 sec)

mysql> SELECT MAX(PrizeMoney),MIN(PrizeMoney),SUM(PrizeMoney), AVG(PrizeMoney) FROM games;
+-----------------+-----------------+-----------------+-----------------+
| MAX(PrizeMoney) | MIN(PrizeMoney) | SUM(PrizeMoney) | AVG(PrizeMoney) |
+-----------------+-----------------+-----------------+-----------------+
|           25000 |            5000 |           77000 |      11000.0000 |
+-----------------+-----------------+-----------------+-----------------+
1 row in set (0.01 sec)

mysql> SELECT G.GCode,G.GameName,P.NAME FROM games G,Players P WHERE P.GCode=G.GCode;
+-------+-------------+---------+
| GCode | GameName    | NAME    |
+-------+-------------+---------+
|   101 | Carom       | Arjun   |
|   105 | LawnTennis  | Ravi    |
|   101 | Carom       | Jignesh |
|   103 | TableTennis | Nihal   |
|   104 | Chess       | Sohail  |
+-------+-------------+---------+
5 rows in set (0.00 sec)

mysql> SELECT P.PCode,P.Name,G.PrizeMoney FROM games G,Players P WHERE P.GCode=G.GCode;
+-------+---------+------------+
| PCode | Name    | PrizeMoney |
+-------+---------+------------+
|     1 | Arjun   |       5000 |
|     2 | Ravi    |      25000 |
|     3 | Jignesh |       5000 |
|     4 | Nihal   |       8000 |
|     5 | Sohail  |       9000 |
+-------+---------+------------+
5 rows in set (0.00 sec)

mysql> ALTER TABLE games CHANGE Dt date_of_event DATE;
Query OK, 0 rows affected (0.23 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM games;
+-------+--------------+------------+------------+---------------+
| GCode | GameName     | Eventcount | PrizeMoney | date_of_event |
+-------+--------------+------------+------------+---------------+
|   101 | Carom        |          2 |       5000 | 2019-01-23    |
|   102 | Badminton    |          2 |      10000 | 2019-12-12    |
|   103 | TableTennis  |          4 |       8000 | 2019-02-14    |
|   104 | Chess        |          2 |       9000 | 2019-01-01    |
|   105 | LawnTennis   |          4 |      25000 | 2019-03-19    |
|   106 | NULL         |          1 |      10000 | NULL          |
|   107 | __shooting__ |          2 |      10000 | NULL          |
+-------+--------------+------------+------------+---------------+
7 rows in set (0.00 sec)


mysql> ALTER TABLE Players ADD EMAIL CHAR(30);
Query OK, 0 rows affected (0.63 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM Players;
+-------+---------+-------+-------+
| PCode | NAME    | GCode | EMAIL |
+-------+---------+-------+-------+
|     1 | Arjun   |   101 | NULL  |
|     2 | Ravi    |   105 | NULL  |
|     3 | Jignesh |   101 | NULL  |
|     4 | Nihal   |   103 | NULL  |
|     5 | Sohail  |   104 | NULL  |
+-------+---------+-------+-------+
5 rows in set (0.03 sec)


mysql> ALTER TABLE games CHANGE GameName GameName VARCHAR(20);
Query OK, 0 rows affected (0.19 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM games;
+-------+--------------+------------+------------+---------------+
| GCode | GameName     | Eventcount | PrizeMoney | date_of_event |
+-------+--------------+------------+------------+---------------+
|   101 | Carom        |          2 |       5000 | 2019-01-23    |
|   102 | Badminton    |          2 |      10000 | 2019-12-12    |
|   103 | TableTennis  |          4 |       8000 | 2019-02-14    |
|   104 | Chess        |          2 |       9000 | 2019-01-01    |
|   105 | LawnTennis   |          4 |      25000 | 2019-03-19    |
|   106 | NULL         |          1 |      10000 | NULL          |
|   107 | __shooting__ |          2 |      10000 | NULL          |
+-------+--------------+------------+------------+---------------+
7 rows in set (0.00 sec)


mysql> CREATE TABLE games_COPY AS SELECT * FROM games WHERE 0=1;
Query OK, 7 rows affected (0.40 sec)
Records: 7  Duplicates: 0  Warnings: 0

mysql> DESCRIBE games_COPY;
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| GCode         | int         | NO   |     | NULL    |       |
| GameName      | varchar(20) | YES  |     | NULL    |       |
| Eventcount    | int         | YES  |     | NULL    |       |
| PrizeMoney    | int         | NO   |     | 10000   |       |
| date_of_event | date        | YES  |     | NULL    |       |
+---------------+-------------+------+-----+---------+-------+
5 rows in set (0.15 sec)

mysql> DELETE FROM games WHERE date_of_event IS NULL;
Query OK, 2 rows affected (0.10 sec)

mysql> SELECT * FROM games;
+-------+-------------+------------+------------+---------------+
| GCode | GameName    | Eventcount | PrizeMoney | date_of_event |
+-------+-------------+------------+------------+---------------+
|   101 | Carom       |          2 |       5000 | 2019-01-23    |
|   102 | Badminton   |          2 |      10000 | 2019-12-12    |
|   103 | TableTennis |          4 |       8000 | 2019-02-14    |
|   104 | Chess       |          2 |       9000 | 2019-01-01    |
|   105 | LawnTennis  |          4 |      25000 | 2019-03-19    |
+-------+-------------+------------+------------+---------------+
5 rows in set (0.00 sec)

mysql> UPDATE Players SET GCode=105 WHERE GCode=104;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM Players;
+-------+---------+-------+-------+
| PCode | NAME    | GCode | EMAIL |
+-------+---------+-------+-------+
|     1 | Arjun   |   101 | NULL  |
|     2 | Ravi    |   105 | NULL  |
|     3 | Jignesh |   101 | NULL  |
|     4 | Nihal   |   103 | NULL  |
|     5 | Sohail  |   105 | NULL  |
+-------+---------+-------+-------+
5 rows in set (0.00 sec)

mysql> INSERT INTO games_COPY SELECT * FROM games;
Query OK, 5 rows affected (0.07 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM games_COPY;
+-------+--------------+------------+------------+---------------+
| GCode | GameName     | Eventcount | PrizeMoney | date_of_event |
+-------+--------------+------------+------------+---------------+
|   101 | Carom        |          2 |       5000 | 2019-01-23    |
|   102 | Badminton    |          2 |      10000 | 2019-12-12    |
|   103 | TableTennis  |          4 |       8000 | 2019-02-14    |
|   104 | Chess        |          2 |       9000 | 2019-01-01    |
|   105 | LawnTennis   |          4 |      25000 | 2019-03-19    |
|   106 | NULL         |          1 |      10000 | NULL          |
|   107 | __shooting__ |          2 |      10000 | NULL          |
+-------+--------------+------------+------------+---------------+
7 rows in set (0.00 sec)

mysql> SELECT GameName FROM games WHERE POSITION('B' in GameName)=1 OR POSITION('C' in GameName)=1 GROUP BY date_of_event ORDER BY date_of_event ASC;
+-----------+
| GameName  |
+-----------+
| Chess     |
| Carom     |
| Badminton |
+-----------+
3 rows in set (0.00 sec)

mysql> SELECT PrizeMoney/Eventcount FROM games WHERE MONTH(date_of_event)=01 OR MONTH(date_of_event)=12 GROUP BY PrizeMoney HAVING COUNT(GameName)>1;
Empty set (0.00 sec)

