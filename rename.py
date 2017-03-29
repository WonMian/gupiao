#!/usr/bin/python
#coding:utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
path = '/Users/wangmian/PycharmProjects/ShanghaiZhengquan/testlist'
for filename in os.listdir(path):
    oldname = path + '/' + filename
    filename = path + '/' + filename
    filename = filename.replace(' ','')
    filename = filename.replace('\t','')
    os.rename(oldname,filename)

