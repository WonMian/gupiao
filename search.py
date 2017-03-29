#!/usr/bin/python
# coding:utf-8
import os
import jieba
import re
import sys
import keywordDB
from inverted import word_index
reload(sys)
sys.setdefaultencoding('utf-8')

def search(query):
    results = []

    words = [word for _, (offset, word) in word_index(query)]  # query_words_list
    for word in words:
        txtlist = keywordDB.getTxtId(word)
        if(txtlist):
            results.append(txtlist)
    # doc_set = reduce(lambda x, y: x & y, results) if results else [] #去重
    doc_set = reduce(lambda x,y: set(x).intersection(set(y)),results)
    precise_doc_dic = {}
    if doc_set:
        print "Search for '%s':" % (query)
        for doc in doc_set:
            print keywordDB.findTxtName(doc)
    keywordDB.disconnect()
search('顾清泉')