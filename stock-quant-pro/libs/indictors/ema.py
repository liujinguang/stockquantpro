#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月30日

@author: bob
'''

import talib

def ema(prices, period):
    return talib.EMA(prices, period)

if __name__ == '__main__':
    pass