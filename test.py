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
reload(sys)
sys.setdefaultencoding('utf-8')

try:
    print 1+"qwe"+11
except:
    log.setLogger('haha').exception("Exception Logged")