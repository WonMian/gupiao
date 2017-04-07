#!/usr/bin/python
# -*- coding: utf-8 -*-

# import MySQLdb
# import threading
# import sys
# def db_op_thread_func( i, num_of_op ):
#     conn=MySQLdb.connect(host="localhost",port=3306, user="root",passwd="65671500",db="Shanghai")
#     cursor = conn.cursor()
#     sql = "select * from gonggao"
#     for j in range(0, int(num_of_op) ):
#         cursor.execute( sql )
#         print cursor.fetchone()
#         print "thread", i, ":", " num:", j
#
#     conn.close()
# if __name__ == "__main__":
#     args = sys.argv
#     num_of_thd  = args[1]
#     num_of_op   = args[2]
#     threads = []
#     for i in range( 0, int(num_of_thd) ):
#         threads.append( threading.Thread( target=db_op_thread_func,args=(i, num_of_op ) ) )
#
#     for t in threads:
#         t.start()
#
#     for t in threads:
#         t.join()
# !/usr/bin/env python
import thread, threading
import os, sys, time, getopt, MySQLdb

# optmap = {'user': 'root', 'passwd': '65671500', 'host': 'localhost', 'port': 3306, 'db': 'Shanghai', 'use_unicode': True,
#     'charset': 'utf8'}
#
# db_conn = MySQLdb.connect(**optmap)
# db_cursor = db_conn.cursor()
#
# TOTAL_USERS = 52100
# THREAD_NUM = 16
#
#
# class Run_sp(threading.Thread):
#     def __init__(self, thread_num, user_list):
#         threading.Thread.__init__(self)
#         self.thread_num = thread_num
#         self.user_list = user_list
#
#     def run(self):
#         db_conn = MySQLdb.connect(**optmap)
#         db_cursor = db_conn.cursor()
#         num = 0
#         for user in self.user_list:
#             num += 1
#             account = user[0]
#             password = user[1]
#             db_cursor.execute("Call account_login_('%s','%s')" % (account, password))
#             while 1:
#                 flag = db_cursor.nextset()
#                 if flag != 1: break
#                 db_cursor.fetchall()
#
#             if num % 1000 == 0:
#                 print "Thread %d execute %d users" % (self.thread_num, num)
#         print "thread %d end at [%s]" % (
#         self.thread_num, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#         db_cursor.close()
#         db_conn.close()
#
#
# def main():
#     user_list = []
#     begin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
#     sql = "select Gonggaoming from gonggao limit %d" % TOTAL_USERS
#     db_cursor.execute(sql)
#     result = db_cursor.fetchall()
#     for row in result:
#         # account = row[0]
#         # password = row[1]
#         # user_list.append((account, password))
#         print row
#
#
#     # print "size of user_list:%d"%(len(user_list))
#     #	print user_list
#     #	print user_list[0:2]
#
#     account_in_each_thread = int(TOTAL_USERS / THREAD_NUM)
#     #	print "account_in_each_thread : %d\n"%account_in_each_thread
#
#     thread_list = []
#     for i in range(0, THREAD_NUM):
#         if i != THREAD_NUM - 1:
#             thread_list.append(Run_sp(i, user_list[i * account_in_each_thread:(i + 1) * account_in_each_thread]))
#         else:
#             thread_list.append(Run_sp(i, user_list[i * account_in_each_thread:]))
#         thread_list[i].start()
#
#     end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
#     print "start at [%s]" % begin_time
#     print "end at [%s]" % end_time
#
#
# main()