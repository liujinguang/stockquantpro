#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 30, 2017

@author: hadoop
'''

from utils.emails import send_email
from drawing.drawing_utils import draw_stock_with_multi_periods

import os

if __name__ == '__main__':
    
    file_lst = []
    
    code_id = "399300"
    fname = "/home/hadoop/" + code_id + "-month-week" + ".png"
    draw_stock_with_multi_periods(code_id, ("M", "W"), fname)
    file_lst.append(fname)
# 
#     fname = "/home/hadoop/" + code_id + "-60F-30F" + ".png"
#     draw_stock_with_multi_periods(code_id, ("60", "30"), fname)
#     file_lst.append(fname)

#     fname = "/home/hadoop/" + code_id + "-15F-5F" + ".png"
#     draw_stock_with_multi_periods(code_id, ("15", "5"), fname)
#     file_lst.append(fname)
    
    send_email("jliu@infinera.com", "TEST", "This is a test email, just ignore it", file_lst)  
    
    for f in file_lst:
        os.remove(f)