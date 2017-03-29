#!/usr/bin/python
# coding:utf-8
import os
import jieba
import re
import sys
import keywordDB

reload(sys)
sys.setdefaultencoding('utf-8')


stopWords = open('stopwords.txt', 'r').readlines()

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


def inverted_index_add(inverted, doc_id, doc_index): #倒排索引字典{字段：{文章名：（位置，偏移）}
    for word, locations in doc_index.iteritems():
        indices = inverted.setdefault(word, {})
        indices[doc_id] = locations

      #########
        # txtId = keywordDB.findTxtId(doc_id)
        # if txtId:
        #     txtIdList = keywordDB.getTxtId(word)
        #     if txtIdList:
        #
        #     else:
        #
        #
        # else:
        #     print u"I can't find %s's Id in DB！\n " % doc_id







      ##########

    return inverted


def search(inverted, query):
    words = [word for _, (offset, word) in word_index(query) if word in inverted]  # query_words_list
    results = [set(inverted[word].keys()) for word in words] #[(),(),()...]
    # x = map(lambda old: old+1, x)
    doc_set = reduce(lambda x, y: x & y, results) if results else [] #去重
    precise_doc_dic = {}
    if doc_set:
        for doc in doc_set:
            index_list = [[indoff[0] for indoff in inverted[word][doc]] for word in words]
            offset_list = [[indoff[1] for indoff in inverted[word][doc]] for word in words]
            precise_doc_dic = precise(precise_doc_dic, doc, index_list, offset_list, 1)  # 词组查询
            precise_doc_dic = precise(precise_doc_dic, doc, index_list, offset_list, 2)  # 临近查询
            precise_doc_dic = precise(precise_doc_dic, doc, index_list, offset_list, 3)  # 临近查询

        print ''.join(precise_doc_dic.keys())

        return precise_doc_dic
    else:
        return {}

def precise(precise_doc_dic, doc, index_list, offset_list, range):
    if precise_doc_dic:
        if range != 1:
            return precise_doc_dic  # 如果已找到词组,不需再进行临近查询
    phrase_index = reduce(lambda x, y: set(map(lambda old: old + range, x)) & set(y), index_list)
    phrase_index = map(lambda x: x - len(index_list) - range + 2, phrase_index)

    if len(phrase_index):
        phrase_offset = []
        for po in phrase_index:
            phrase_offset.append(offset_list[0][index_list[0].index(po)])  # offset_list[0]代表第一个单词的字母偏移list
        precise_doc_dic[doc] = phrase_offset
    return precise_doc_dic


if __name__ == '__main__':

    # Build Inverted-Index for documents
    inverted = {}
    # documents = {}
    #
    # doc1 = u"开发者可以指定自己自定义的词典，以便包含jieba词库里没有的词"
    # doc2 = u"军机处长到底是谁，Python Perl"
    #
    # documents.setdefault("doc1", doc1)
    # documents.setdefault("doc2", doc2)

    documents = {}
    for filename in os.listdir('/Users/wangmian/PycharmProjects/ShanghaiZhengquan/testlist'):  #读入文件做KEY
        f = open('/Users/wangmian/PycharmProjects/ShanghaiZhengquan/testlist/' + filename).read() #Value
        documents.setdefault(filename.decode('utf-8'), f)
    for doc_id, text in documents.iteritems():
        doc_index = inverted_index(text)  #一篇文章的倒排索引
        inverted_index_add(inverted, doc_id, doc_index)

    # Print Inverted-Index
    # for word, doc_locations in inverted.iteritems():
    #     print word, doc_locations

    # Search something and print results
    queries = ['中国']
    for query in queries:
        result_docs = search(inverted, query)
        print "Search for '%s': %s" % (query,u','.join(result_docs.keys()))  # %s是str()输出字符串%r是repr()输出对象
        def extract_text(doc, index):
            return documents[doc].decode('utf-8')[index:index + 30].replace('\n', ' ')


        if result_docs:
            for doc, offsets in result_docs.items():
                for offset in offsets:
                    print '   - %s...' % extract_text(doc, offset)
        else:
            print 'Nothing found!'
    keywordDB.disconnect()
