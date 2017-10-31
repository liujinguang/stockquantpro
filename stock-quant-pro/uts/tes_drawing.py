#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 30, 2017

@author: hadoop
'''

from libs.drawing.drawing_utils import draw_stock_with_multi_periods

if __name__ == '__main__':
    code_id = "399300"
    fname = "/home/hadoop/" + code_id + "-month-week" + ".png"
    draw_stock_with_multi_periods(code_id, ("M", "W"), fname)    