# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月30日

@author: bob
'''

import pandas as pd
import tushare as ts
from utils.time_utils import is_alert_needed
from utils.log import log
from database import db_crud
from utils.constants import GOLDEN_CROSS, DEAD_CROSS


def _expma(period, m, exp_ma, prices):
    '''
    指数平滑均线函数.
    以prices计算，可以选择收盘、开盘价等价格，period为时间周期，
    m用于计算平滑系数a=m/(period+1)，exp_ma为前一日值指数评价值
    '''
    a = m / (period + 1.0)
    return a * prices + (1 - a) * exp_ma

def macd(prices, fast=12, slow=26, signal=9, m=2.0):
    '''
    12日EMA的计算：EMA12 = 前一日EMA12 X 11/13 + 今日收盘 X 2/13
    
    26日EMA的计算：EMA26 = 前一日EMA26 X 25/27 + 今日收盘 X 2/27
    
        差离值（DIF）的计算： DIF = EMA12 - EMA26，即为talib-MACD返回值macd
    
        根据差离值计算其9日的EMA，即离差平均值，是所求的DEA值。
        今日DEA = （前一日DEA X 8/10 + 今日DIF X 2/10），即为talib-MACD返回值signal
    
    DIF与它自己的移动平均之间差距的大小一般BAR=（DIF-DEA)2，即为MACD柱状图。
        但是talib中MACD的计算是bar = (dif-dea)1    
    '''
    expma12_1 = pd.ewma(prices, span=fast)  
    expma26_1 = pd.ewma(prices, span=slow) 

    expma12_2 = _expma(fast, m, expma12_1, prices)
    expma26_2 = _expma(slow, m, expma26_1, prices)
    
    diff2 = expma12_2 - expma26_2
    dea2 = pd.ewma(diff2, span=signal)
    bar2 = 2 * (diff2 - dea2)
    
    return diff2, dea2, bar2

def get_stock_macd(code_id, ktype, data=None, index=False):
    '''
    '''
    if data is None:
        data = ts.get_k_data(code_id, ktype=ktype, index=index)
    
    return macd(data['close'])


def is_macd_golden_cross_now(stock_entity, ktype, data=None, index=False):
    '''
    is the MACD in golden cross status
    '''
    log.info("Start to check " + stock_entity.codeId + " " + ktype + 
             "F MACD golden cross")
    if data is None:
        data = ts.get_k_data(stock_entity.codeId, ktype=ktype, index=index)
    
    diff, dea, bar = get_stock_macd(stock_entity.codeId, ktype, data=data, index=index)

    #check the gold cross for this kind of period, 60F is too long, so it alerts when it's neer to
    #golden cross
    if bar.values[-2] < 0 and bar.values[-1] >= 0 and is_alert_needed(stock_entity, ktype, GOLDEN_CROSS):
        db_crud.update_alert_time(stock_entity, ktype, GOLDEN_CROSS)
        log.info("stock " + stock_entity.codeId + " has a MACD golden cross for " + 
                 ktype + "F period ")
        return True
  
    return False

def is_macd_dead_cross_now(stock_entity, ktype, data=None, index=False):
    '''
    is the MACD in golden cross status
    '''
    log.info("Start to check " + stock_entity.codeId + " " + ktype + 
             "F MACD dead cross")
    if data is None:
        data = ts.get_k_data(stock_entity.codeId, ktype=ktype, index=index)
    
    diff, dea, bar = get_stock_macd(stock_entity.codeId, ktype, data=data, index=index)

    #check the gold cross for this kind of period, 60F is too long, so it alerts when it's neer to
    #golden cross
    if bar.values[-2] > 0 and bar.values[-1] <= 0 and is_alert_needed(stock_entity, ktype, DEAD_CROSS):
        db_crud.update_alert_time(stock_entity, ktype, DEAD_CROSS)
        log.info("stock " + stock_entity.codeId + " has a MACD dead cross for " + ktype + "F period ")
        return True
  
    return False

if __name__ == '__main__':
    pass
