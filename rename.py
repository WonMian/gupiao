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
def renameFile():
    path = '/Users/wangmian/PycharmProjects/ShanghaiZhengquan/testlist'
    for filename in os.listdir(path):
        oldname = path + '/' + filename
        filename = path + '/' + filename
        filename = filename.replace(' ','')
        filename = filename.replace('\t','')
        os.rename(oldname,filename)
def updateDB(newname,ID):

    cur.execute(
        "update gonggao set Gonggaoming = %s where Id=%s" , (newname, ID)
    )
    conn.commit()
def renameDB():
    cur.execute(
        "SELECT * FROM gonggao"
)
    lines = cur.fetchall()
    for line in lines:
        filename = line[1]
        filename = filename.replace(' ','')
        filename = filename.replace('\t','')
        print filename
        print line[0]
        updateDB(filename,line[0])
    cur.close()
    conn.close()

renameDB()

