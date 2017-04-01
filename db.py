#coding:utf-8
import MySQLdb
import time

conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '65671500',
    db = 'Shanghai',
    charset="utf8"
)
cur = conn.cursor()
# localtime = time.strftime("%Y-%m-%d",time.localtime())
# import mysql.connector as mariadb
#
# conn = mariadb.connect(
#     user='root',
#     password='Onlyou+wmnb1',
#     database='GUPIAO',
#     host = 'localhost',
#     port = 3306,
#     charset = 'utf8'
#     )
# cur = conn.cursor()
# #
# cur.execute("CREATE TABLE IF NOT EXISTS \
#     gonggao(Id INT PRIMARY KEY AUTO_INCREMENT,\
#     Gonggaoming VARCHAR(255),\
#     Urlpath VARCHAR(255),\
#     OrderDate timestamp not null DEFAULT NOW())"
# )
def insert(name,urlpath):
    sqli="insert into gonggao(Gonggaoming,Urlpath) values(%s,%s)"
    cur.execute(sqli,(name,urlpath))
    conn.commit()
def inDB():
    cur.execute(
        "SELECT * FROM gonggao"
    )
    lines = cur.fetchall()
    return lines


def disconnect():
    cur.close()
    conn.close()

