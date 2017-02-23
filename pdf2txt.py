#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import os
import pdb
from bs4 import BeautifulSoup
import json
import re
import MySQLdb
import db
#os.chdir(r'F:\test')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}


def pdfToTxt(filename):
    path = os.path.abspath(os.path.dirname("pdf2txt.py")) + '/txtlist'
    if not os.path.isdir(path):
        os.mkdir(path)
    txtname = path + '/' + filename + '.txt'
    path = os.path.abspath(os.path.dirname("pdf2txt.py")) + '/pdflist/' + filename + '.pdf'
    db.insert(filename,path)  #存入数据库

    fp = open(path, 'rb')
    #来创建一个pdf文档分析器
    parser = PDFParser(fp)
    #创建一个PDF文档对象存储文档结构
    document = PDFDocument(parser)
    # 检查文件是否允许文本提取
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建一个PDF资源管理器对象来存储共赏资源
        rsrcmgr=PDFResourceManager()
        # 设定参数进行分析
        laparams=LAParams()
        # 创建一个PDF设备对象
        # device=PDFDevice(rsrcmgr)
        device=PDFPageAggregator(rsrcmgr,laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter=PDFPageInterpreter(rsrcmgr,device)
        # 处理每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout=device.get_result()
            for x in layout:
                if(isinstance(x,LTTextBoxHorizontal)):
                    with open(txtname,'a') as f:
                        f.write(x.get_text().encode('utf-8')+'\n')
def getShanghaiPdf(annoucement):


    pdfUrl = annoucement['href']

    path = os.path.abspath(os.path.dirname("pdf2txt.py")) + '/pdflist'
    if not os.path.isdir(path):
        os.mkdir(path)
    pdfname = path + '/'  + annoucement.get_text() + '.pdf'
    r = requests.get(pdfUrl,headers=headers)
    print u'正在获取'+annoucement.get_text()

    with open(pdfname,"wb") as pdf:
        pdf.write(r.content)
    pdfToTxt(annoucement.get_text().encode('utf8'))
    # pdfToTxt(annoucement['title']+'.pdf')
    # pdfparser(pdfname)

def getNewestAnnoucement():
    url = 'http://www.sse.com.cn/disclosure/listedinfo/announcement/s_docdatesort_desc_2016openpdf.htm'
    s = requests.session()
    data = s.post(url,headers=headers)
    # annoucements = re.findall('<a href="(.*?)" target.*?>(.*?)</a.*?</em>',data.content.decode("utf-8", 'ignore'),re.S)
    # for annoucement in annoucements:
    #     print annoucement[0]+annoucement[1]
    soup = BeautifulSoup(data.content, 'lxml')
    # print soup
    # a = soup.select('dl')
    # print a
    annoucement1 = soup.find_all(href=re.compile('http://static.sse.com.cn/disclosure'),target=re.compile('_blank'))
    num = 0
    for annoucements in annoucement1:
        if num % 2 == 0:
            try:
                getShanghaiPdf(annoucements)
            except Exception,e:
                print Exception,":",e

        num += 1



getNewestAnnoucement()
db.disconnect()