#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import base64
import config
reload(sys)

sys.setdefaultencoding('utf-8')

conn = config.db()
cur = conn.cursor()

#
# cur.execute("CREATE TABLE IF NOT EXISTS \
# inverted(Id INT PRIMARY KEY AUTO_INCREMENT,\
#         keyword varchar(255),\
#         txtID text) "
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
    cur.execute('SELECT Id FROM gonggao WHERE Gonggaoming = %s LIMIT 1', (txtname.decode('UTF8'),))
    result = cur.fetchone()
    if result:
        return int(result[0])
    return None

def findTxtName(Id):
    cur.execute( 'SELECT Gonggaoming FROM gonggao where Id = %s LIMIT 1', (Id,) )
    result = cur.fetchone()
    if result:
        return result[0]
    return None

def getTxtId(keyword):
    cur.execute("SELECT txtID FROM inverted WHERE keyword = %s LIMIT 1",(keyword.decode('UTF8'), ))
    result = cur.fetchone()
    if result:
        result = decode_base64(result[0])
        return eval(result)
    return None

def disconnect():
    cur.close()
    conn.close()
# def getTxtId(keyword):
#     cur.execute(
#         "SELECT * FROM inverted"
#     )
#     lines = cur.fetchall()
#     for line in lines:
#         if keyword.decode('UTF8') in line:
#             result = decode_base64(line[2])
#             # print result
#
#             return eval(result)
#     return


def decode_base64(data):
    """Decode base64, padding being optional.
    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.
    """
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'=' * missing_padding
    return base64.decodestring(data)

