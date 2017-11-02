#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 30, 2017

@author: hadoop
'''

from utils.log import log 

import os
import sys
from datetime import datetime

if __name__ == '__main__':
    log.info("hello world")
    
#     rdir = 'd:\\quant\\' + datetime.now().strftime("%Y-%m-%d")
#     print rdir
#     
#     if os.path.exists(rdir):
#         print "hello"
#     else:
#         os.mkdir(rdir)
    stock = {
        "603226" : "菲林格尔",
        "603225" : "新凤鸣",
        "603226" : "菲林格尔",
        "603225" : "新凤鸣",        
    }
    
    print stock.keys()
    