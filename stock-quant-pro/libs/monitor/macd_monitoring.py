#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

import tushare as ts
from utils.time_utils import get_start_date
from indictors.macd import macd

def monitor_stock_macd(code_id, ktype, index=False):
    '''
    '''
    start = get_start_date(ktype)
    data = ts.get_k_data(code_id, ktype=ktype, index=index, start=start)
    data = data[data.date > start]
    
    diff, dea, bar = macd(data['close'])
    
    if bar[-2] <= 0 and bar[-1] > 0:
        return True
    else:
        return False
    

if __name__ == '__main__':
    pass