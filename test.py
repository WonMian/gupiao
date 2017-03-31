#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os
import pdb
from bs4 import BeautifulSoup
import json
import re
import MySQLdb
import db
import sys
from chardet import detect
import math
import log
import config
reload(sys)
sys.setdefaultencoding('utf-8')
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) \
#                     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
# url = 'http://query.sse.com.cn/infodisplay/queryLatestBulletinNew.do?jsonCallBack=jsonpCallback73960&isPagination=true&productId=&keyWord=&reportType2=&reportType=ALL&beginDate=2017-03-01&endDate=2017-03-01&pageHelp.pageSize=25&pageHelp.pageCount=50&pageHelp.pageNo=1&pageHelp.beginPage=1&pageHelp.cacheSize=1&pageHelp.endPage=5&_=1490935508348'
# s = requests.session()
# data = s.get(url,headers = headers)
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

cur.execute("CREATE TABLE  \
   test(Id INT PRIMARY KEY AUTO_INCREMENT,\
   OrderDate timestamp not null)")