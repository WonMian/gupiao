#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import os
# import pdb
from bs4 import BeautifulSoup
import re
import db
import sys
import inverted
import keywordDB
import config
import time
reload(sys)
sys.setdefaultencoding('utf-8')
#os.chdir(r'F:\test')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
txtList = db.inDB()  #获取当前已入库的文章
filenameList = []
path = config.path
def pdfToTxt(filename,urlpath):
    # filename = filename.replace(' ','')
    # filename = filename.replace('\t','')
    txtPath = path + '/txtlistSH'
    if not os.path.isdir(txtPath):
        os.mkdir(txtPath)
    txtname = txtPath + '/' + filename.encode('UTF-8') + '.txt'
    pdfPath = path + '/pdflist/' + filename.encode('UTF-8') + '.pdf'


    fp = open(pdfPath, 'rb')
    #来创建一个pdf文档分析器
    parser = PDFParser(fp)
    #创建一个PDF文档对象存储文档结构
    document = PDFDocument(parser)
    # 检查文件是否允许文本提取
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建一个PDF资源管理器对象来存储共赏资源
        rsrcmgr = PDFResourceManager()
        # 设定参数进行分析
        laparams = LAParams()
        # 创建一个PDF设备对象
        # device=PDFDevice(rsrcmgr)
        device = PDFPageAggregator(rsrcmgr, laparams = laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # 处理每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(txtname, 'a') as f:
                        f.write(x.get_text().encode('utf-8') + '\n')
    db.insert(filename,urlpath)  #存入数据库
    localtime = time.ctime(time.time())
    print localtime + '\t' + filename + '\t' + u'已入库，将做倒排索引处理\n'
    filenameList.append(filename)
    # inverted.invertedAPI(filename)



def getShanghaiPdf(annoucement):
    pdfUrl = annoucement['href']
    pdfPath = path + '/pdflist'
    if not os.path.isdir(pdfPath):
        os.mkdir(pdfPath)
    filename = annoucement.get_text().encode('utf-8')
    filename = filename.replace(' ','')
    filename = filename.replace('\t','')
    for list in txtList:
        if filename.decode('UTF8') in list:
            print filename + '\talready in db!\n'
            return
    pdfname = pdfPath + '/'  + filename + '.pdf'
    # pdfname = pdfname.replace(' ','')
    # pdfname = pdfname.replace('\t','')
    r = requests.get(pdfUrl,headers=headers)
    print u'正在获取'+annoucement.get_text()

    with open(pdfname,"wb") as pdf:
        pdf.write(r.content)
    pdfToTxt(filename,pdfUrl)
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
    annoucement1 = soup.find_all(href = re.compile('http://static.sse.com.cn/disclosure'),
                                 target = re.compile('_blank'))
    num = 0
    for annoucements in annoucement1:
        if num % 2 == 0:
            try:
                getShanghaiPdf(annoucements)
            except Exception, e:
                print Exception, ":", e

        num += 1


getNewestAnnoucement()
f = open(path + '/haveInverted.txt','a+')
for filename in filenameList:
    try:
        inverted.invertedAPI(filename)
        localtime = time.strftime("%Y-%m-%d",time.localtime())
        f.write(localtime + ':' + filename + '\n')
    except Exception,e:
        print Exception,":",e
f.close()
keywordDB.disconnect()
os.system('rm -rf ' + path + '/pdflist/*')

# keywordDB.disconnect()
os.system('rm -rf ' + path + '/pdflist/*')
