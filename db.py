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

# localtime = time.strftime("%Y-%m-%d",time.localtime()
cur = conn.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS \
# gonggao(Id INT PRIMARY KEY AUTO_INCREMENT,\
#     Gonggaoming VARCHAR(255),\
#     Path VARCHAR(255),\
#     OrderDate datetime NOT NULL DEFAULT NOW())"
# )
def insert(name,path):
    sqli="insert into gonggao(Gonggaoming,Path) values(%s,%s)"
    cur.execute(sqli,(name,path))
    conn.commit()

def disconnect():
    cur.close()
    conn.close()


# cur.execute("insert into gonggao VALUES ('1','华北制药关于收到上海证券交易所问询函的公告.txt', \
#           '/Users/wangmian/PycharmProjects/ShanghaiZhengquan/txtlist/华北制药关于收到上海证券交易所问询函的公告.txt',\
#           localtime)"