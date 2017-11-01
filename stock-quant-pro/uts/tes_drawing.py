#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 30, 2017

@author: hadoop
'''

from drawing.drawing_utils import draw_stock_with_multi_periods2
import numpy as np
import database.db as db
from indictors.macd import get_stock_macd

if __name__ == '__main__':
    code_id = "002475"
    fname = "/home/hadoop/" + code_id + "-month-week" + ".png"
    draw_stock_with_multi_periods2(code_id, ("W", "D", "60", "30", "15", "5"), fname, index=False)
#     draw_stock_with_multi_periods(code_id, ("15", "5"), fname, index=True)
#     num = 6    
#     a = np.arange(1, 3*num + 1).reshape(3*num/2, 2)
#     print a
#     for i in xrange(num):
#         print a[i/2*3][i%2], a[i/2*3 + 1][i%2], a[i/2 *3+2][i%2]

#     diff, dea, bar = get_stock_macd(code_id, "30", db.is_index(code_id))
#     print diff.values[-1]
    