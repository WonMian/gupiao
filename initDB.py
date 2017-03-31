#coding:utf-8
import time
import mysql.connector as mariadb
conn = mariadb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'Onlyou+wmnb1',
    database = 'GUPIAO',
    charset="utf8"
)

# localtime = time.strftime("%Y-%m-%d",time.localtime()
cur = conn.cursor()
def dropTB():
    cur.execute(
        "DROP TABLE gonggao"
    )
    cur.execute(
        "DROP TABLE inverted"
    )
def createTB():
    cur.execute("CREATE TABLE  \
       gonggao(Id INT PRIMARY KEY AUTO_INCREMENT,\
       Gonggaoming VARCHAR(100),\
       Urlpath VARCHAR(255),\
       OrderDate timestamp not null DEFAULT NOW())"
    )


    cur.execute("CREATE TABLE  \
    inverted(Id INT PRIMARY KEY AUTO_INCREMENT,\
            keyword varchar(255),\
            txtID text) "
    )
#dropTB()
#createTB()
conn.commit()
cur.close()
conn.close()
