# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月30日

@author: bob
'''

from utils.log import log
from utils.constants import GOLDEN_CROSS, DEAD_CROSS
from utils.time_utils import is_alert_needed

import talib
import numpy as np
import tushare as ts
import database.db_crud as db_crud


def ema(prices, period):
    return talib.EMA(prices, period)

def is_prices_above_ema120(bid, data):
    '''
    '''
    ema120 = ema(np.array(data['close']), 120)
    log.info("EMA120 price is " + str(ema120[-1]))
    if bid >= ema120[-1]:
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
    
def is_prices_above_ema_with_period(code_id, data, bid, period):
    '''
    Check if the prices is above the MA Period
    '''
    ema_tmp = ema(np.array(data['close']), period)
    if bid >= ema_tmp[-1]:
        log.info("==========Stock " + code_id + " EMA:" + str(ema_tmp[-1]) 
                 + ", bid:" + str(bid) + "============")
        return True
    else:
        return False    
    
def is_ema_golden_cross_now(stock_entity, ktype, data=None):
    '''
    is the MA in golden cross status
    '''
    log.info("Start to check " + stock_entity.codeId + " " + ktype + 
             "F MA golden cross")
    if data is None:
        data = ts.get_k_data(stock_entity.codeId, ktype=ktype, 
                             index=stock_entity.isIndex)
    
    ema05 = ema(np.array(data['close']), 5)
    ema10 = ema(np.array(data['close']), 10)
    
    if (ema05[-1] >= ema10[-1]) and (ema05[-2] < ema10[-2]) \
        and is_alert_needed(stock_entity, ktype, GOLDEN_CROSS):
        db_crud.update_alert_time(stock_entity, ktype, GOLDEN_CROSS)
        log.info("stock " + stock_entity.codeId + " has a MA golden cross for " + 
                 ktype + "F period ")
        return True
            
    return False

def is_macd_dead_cross_now(stock_entity, ktype, data=None):
    '''
    is the MA in golden cross status
    '''
    log.info("Start to check " + stock_entity.codeId + " " + ktype + 
             "F MA dead cross")
    if data is None:
        data = ts.get_k_data(stock_entity.codeId, ktype=ktype, 
                             index=stock_entity.isIndex)
    
    ema05 = ema(np.array(data['close']), 5)
    ema10 = ema(np.array(data['close']), 10)
    
    if (ema05[-1] >= ema10[-1]) and (ema05[-2] < ema10[-2]) \
        and is_alert_needed(stock_entity, ktype, DEAD_CROSS):
        db_crud.update_alert_time(stock_entity, ktype, DEAD_CROSS)
        log.info("stock " + stock_entity.codeId + " has a MA dead cross for " + 
                 ktype + "F period ")
        return True
            
    return False

if __name__ == '__main__':
    pass
