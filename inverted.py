#!/usr/bin/python
# coding:utf-8
import jieba
import re
import sys
import keywordDB
import  config
reload(sys)
sys.setdefaultencoding('utf-8')
path = config.path
stopWords = open(path + '/stopwords.txt', 'r').readlines()

def word_split(text):   #分词
    word_list = []
    pattern = re.compile(u'[\u4e00-\u9fa5]+')

    jieba_list = list(jieba.cut(text))  #导入结巴分词
    time = {}
    for i, c in enumerate(jieba_list):  #enumerate()枚举，文件太大时可以此函数

        if c in time:  # 记录出现次数
            time[c] += 1
        else:
            time.setdefault(c, 0) != 0

        if pattern.search(c):  # if Chinese
            word_list.append((len(word_list), (text.index(c, time[c]), c))) #(长度，（word在文中不同的位置,keyword）)
            continue
        if c.isalnum():  # if English or number
            word_list.append((len(word_list), (text.index(c, time[c]), c.lower())))  # include normalize

    return word_list


def words_cleanup(words):
    cleaned_words = []
    for index, (offset, word) in words:  # words-(word index for search,(letter offset for display,word))
        if word in stopWords:
            continue
        cleaned_words.append((index, (offset, word)))
    return cleaned_words


def word_index(text):
    words = word_split(text)    #返回的数组[数组中的位置，（在文章中的位置，字段）]
    words = words_cleanup(words)
    return words


def inverted_index(text):   #一篇文本建立倒排索引 word-[(位置，偏移)]
    inverted = {}

    for index, (offset, word) in word_index(text):
        locations = inverted.setdefault(word, [])  #{word:[(),(),()...]}
        locations.append((index, offset))

    return inverted


def inverted_index_add(doc_id, doc_index): #txtID

    for word, locations in doc_index.iteritems():
        # indices = inverted.setdefault(word, {})
        # indices[doc_id] = locations
      #########
        try:
            txtIdList = keywordDB.getTxtId(word)
            if txtIdList:
                if doc_id in txtIdList:
                    print "%s was already in %s\n" % (doc_id,word)
                else:
                    txtIdList.append(doc_id)
                    keywordDB.updateKeyword(word,txtIdList)
                    print "updateKeyword:%s\n" % word
            else:
                listInit = []
                listInit.append(doc_id)
                keywordDB.insertKeyword(word,listInit)
                print "insert %s into DB\n " % word
        except Exception, e:
            print Exception, ":", e
      ##########
    # return inverted

def invertedAPI(filename):
    # Build Inverted-Index for documents
    # documents = {}
    #
    # doc1 = u"开发者可以指定自己自定义的词典，以便包含jieba词库里没有的词"
    # doc2 = u"军机处长到底是谁，Python Perl"
    #
    # documents.setdefault("doc1", doc1)
    # documents.setdefault("doc2", doc2)


    f = open(path + '/txtlistSH/' + filename.encode('UTF-8') + '.txt').read()  # Value
    txtID = keywordDB.findTxtId(filename)
    if txtID:
        doc_index = inverted_index(f)  # 一篇文章的倒排索引
        inverted_index_add(txtID, doc_index)
    else:
        print u"I can't find %s's Id in DB！\n " % filename

