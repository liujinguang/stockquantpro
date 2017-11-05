#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

from datetime import datetime, timedelta

if __name__ == '__main__':
#     a = datetime.now() + timedelta(hours=2, minutes=15)
#     print (a -datetime.now()).total_seconds()
#     print a.strftime("%Y-%m-%d-%H-%M")
#     working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#     STOCK_START_AM_HOUR = 9
#     STOCK_START_AM_MIN = 30
#     STOCK_STOP_AM_HOUR = 11
#     STOCK_STOP_AM_MIN = 30
#     now = datetime.now() + timedelta(days=0)
#     week_day = now.strftime("%A")
#     
#     if now.strftime("%A") in working_days:
#         print "Working day"
#         
#         
#     
#     print type(now.minute)
    
#     b =  a - datetime.now()
#     print b.total_seconds()
    print type(datetime.strptime("2017-11-04 11:20:33", "%Y-%m-%d %H:%M:%S"))
    
    print datetime.now().strftime("%Y-%m-%d %H:%M:%S")