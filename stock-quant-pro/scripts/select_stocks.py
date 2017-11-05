#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月4日

@author: bob
'''
# from database.db_crud import db_crud
from utils.log import log

import numpy as np
import tushare as ts
import os
import database.db_crud as db_crud

from indictors.ema import is_prices_above_ema120
from indictors.macd import get_stock_macd
from utils.utilities import get_charts_root_directory
from drawing.drawing_utils import draw_stock_with_candlestick_macd

def is_stock_neer_golen_cross(stock_id):
    '''
    '''
    log.info("Start to check stock " + stock_id)
    try:
        quotes = ts.get_realtime_quotes(stock_id)
    except Exception:
        pass
    
    bid = float(quotes["bid"].values[0])
    log.info(stock_id +" current bid " + str(bid))
    
    #Check Day here, must stand up MA20
#             data_D = ts.get_k_data(code_id, ktype="D")
#             if not is_prices_above_ema20(bid, data_D):
#                 log.info(code_id + "'s prices under Day MA20")
#                 continue
    

    #Check 30F here
    data_30F = ts.get_k_data(stock_id, ktype="30")
    if not is_prices_above_ema120(bid, data_30F):
        return False
    
    diff, dea, bar = get_stock_macd(stock_id, "30", data=data_30F)
    
    _bar = np.array(bar[-10:])
    _diff = np.array(diff[-10:])
    _dea = np.array(dea[-10:])
    
    if _bar[-1] < 0 and _bar.argmin() <=5 and _bar[-1] > _bar[-2] \
        and _bar[-2] > _bar[-3] and _bar[-4] > _bar[-5] \
        and _dea.min() > 0:
        return True
    else:
        return False
    
def is_day_period_golen_cross(stock_id, ktype):
    log.info("Start to check stock " + stock_id)
    try:
        quotes = ts.get_realtime_quotes(stock_id)
    except Exception:
        return False
    
    bid = float(quotes["bid"].values[0])
    log.info(stock_id +" current bid " + str(bid))
    
    #Check 30F here
    data_d = ts.get_k_data(stock_id, ktype)
    if not is_prices_above_ema120(bid, data_d):
        return False    
    
    diff, dea, bar = get_stock_macd(stock_id, ktype, data=data_d)
    if bar.values[-1] >= 0 and bar.values[-2] < 0:
        return True
    else:
        return False
    
if __name__ == '__main__':
    stock_entities = db_crud.get_stock_in_market()
     
    for entity in stock_entities:
        code_id = entity.codeId
        if is_day_period_golen_cross(code_id):
            log.info("Day golden cross: " + code_id)
            entity.isObserved = True
    
#     code_id = "300450"
#     fname = get_charts_root_directory() + os.sep + code_id + ".png"
#     draw_stock_with_candlestick_macd(code_id, ("W", "D", "30", "15"), fname)
    