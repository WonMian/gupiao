#coding:utf-8
import jieba



article = open(u"/Users/wangmian/PycharmProjects/ShanghaiZhengquan/txtlist/*ST云维管理人关于出资人组会议召开情况的公告.pdf.txt","r").read()
words = jieba.cut(article, cut_all = False)
for word in words:
    print word
