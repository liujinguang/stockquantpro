#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

from datetime import datetime, timedelta

if __name__ == '__main__':
    a = datetime.now() + timedelta(hours=2, minutes=15)
    print (a -datetime.now()).total_seconds()
    print a.strftime("%Y-%m-%d-%H-%M")
#     b =  a - datetime.now()
#     print b.total_seconds()