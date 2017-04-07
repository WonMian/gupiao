import MySQLdb
import mysql.connector as mariadb

def mysql():
    conn = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = '65671500',
        db = 'Shanghai',
        charset="utf8"
    )
    return conn
def maria():
    conn = mariadb.connect(
        user='root',
        password='Onlyou+wmnb1',
        database='GUPIAO',
        host = 'localhost',
        port = 3306,
        charset = 'utf8'
        )
    return conn
def db():
    return mysql()
    # return maria()

path = '/Users/wangmian'