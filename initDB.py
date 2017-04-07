#coding:utf-8
import time
import os
import config

conn = config.db()
cur = conn.cursor()
def dropTB():
    cur.execute(
        "DROP TABLE gonggao"
    )
    cur.execute(
        "DROP TABLE inverted"
    )
    os.system("rm -rf " + config.path + "/txtlistSH/*")
    os.system("rm -rf " + config.path + "/pdflist/*")
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
dropTB()
createTB()
conn.commit()
cur.close()
conn.close()
