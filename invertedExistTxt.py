#! /usr/bin/python
# -*- coding:UTF8 -*-
from inverted import invertedAPI
import os
import config
def invertedNow():
    f = open(config.path + '/haveInverted.txt', 'ra+')
    haveInvertedName = f.readlines()

    for filename in os.listdir(config.path + '/txtlistSH'):
        # for filename in filenameList:
        filename = filename.replace('.txt', '')
        for a in haveInvertedName:
            if filename in a:
                print filename + '已经过处理，将不再进行处理'
            else:
                try:
                    invertedAPI(filename)
                    f.write(filename + '\n')
                    print '已处理' + filename
                except Exception, e:
                    print Exception, ":", e

invertedNow()