#! /usr/bin/python
# -*- coding:UTF8 -*-
from inverted import invertedAPI
import os
import config
import time
def invertedNow():
    f = open(config.path + '/haveInverted.txt', 'r+')
    haveInvertedName = f.read()
    f.close()
    f = open(config.path + '/haveInverted.txt', 'a+')

    for filename in os.listdir(config.path + '/txtlistSH'):
        # for filename in filenameList:
        filename = filename.replace('.txt', '')
        if filename in haveInvertedName:
            print filename + '已经过处理，将不再进行处理'
        else:
            try:
                invertedAPI(filename)
                f.write(filename + '\n')
                f.flush()
                print '已处理' + filename
            except Exception, e:
                print Exception, ":", e
    f.close()

while 1:
    count = 1
    invertedNow()
    print '\nHave inverted\t' + count + '\ttimes\n'
    count += 1
    time.sleep(43200)
