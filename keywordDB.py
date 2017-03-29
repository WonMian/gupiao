#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
import sys
import base64

reload(sys)

sys.setdefaultencoding('utf-8')

conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '65671500',
    db = 'Shanghai',
    charset="utf8"
)
cur = conn.cursor()
#
# cur.execute("CREATE TABLE IF NOT EXISTS \
# inverted(Id INT PRIMARY KEY AUTO_INCREMENT,\
#         keyword varchar(255),\
#         txtID tinytext) "
# )
def insertKeyword(keyword,txtID):
    base64str = base64.b64encode(str(txtID))
    sqli="insert into inverted(keyword,txtID) values(%s,%s)"
    cur.execute(sqli, (keyword, base64str))
    conn.commit()
def updateKeyword(keyword,txtID):
    base64str = base64.b64encode(str(txtID))

    cur.execute(
        "update inverted set txtID=%s where keyword=%s", (base64str, keyword.decode('UTF8'))
    )
    conn.commit()
def findTxtId(txtname):
    cur.execute(
        "SELECT * FROM gonggao"
    )
    lines = cur.fetchall()
    for line in lines:
        if txtname.decode('UTF8') in line:

            return int(line[0])
    return
def findTxtName(Id):
    cur.execute(
        "SELECT * FROM gonggao"
    )
    lines = cur.fetchall()
    for line in lines:
        if Id in line:
            return line[1]
    return
def getTxtId(keyword):
    cur.execute(
        "SELECT * FROM inverted"
    )
    lines = cur.fetchall()
    for line in lines:
        if keyword.decode('UTF8') in line:
            str = base64.b64decode(line[2])
            return eval(str)
    return

def disconnect():
    cur.close()
    conn.close()

