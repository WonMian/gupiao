#coding:utf-8
import time
import config
conn = config.db()
cur = conn.cursor()

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

# print localtime + '：as'