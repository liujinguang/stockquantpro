#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月30日

@author: bob
'''

from utils.log import log

import talib
import numpy as np


def ema(prices, period):
    return talib.EMA(prices, period)

def is_prices_above_ema120(bid, data):
    '''
    '''
    ema120 = ema(np.array(data['close']), 120)
    if bid >= ema120[-1]:
        log.info("==========EAM120:" + str(ema120[-1]) + ", bid:" + str(bid) + "============")
        return True
    else:
        return False
    
def is_prices_above_ema20(bid, data):
    '''
    '''
    ema20 = ema(np.array(data['close']), 20)
    if bid >= ema20[-1]:
        log.info("==========EAM20:" + str(ema20[-1]) + ", bid:" + str(bid) + "============")
        return True
    else:
        return False

if __name__ == '__main__':
    pass