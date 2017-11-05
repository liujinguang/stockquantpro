#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月4日

@author: bob
'''

from utils.log import log

import numpy as np
import tushare as ts
import os
import database.db_crud as db_crud

from indictors.ema import is_prices_above_ema120
from indictors.macd import get_stock_macd
from utils.utilities import get_charts_root_directory
from drawing.drawing_utils import draw_stock_with_candlestick_macd

def is_ma_30f_satisfied(stock_id):
    '''
    '''
    log.info("Start to check stock " + stock_id)
    try:
        quotes = ts.get_realtime_quotes(stock_id)
    except Exception:
        return False
    
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
    
    return True

def is_ma_60f_satisfied(stock_id):
    '''
    '''
    log.info("Start to check stock " + stock_id)
    try:
        quotes = ts.get_realtime_quotes(stock_id)
    except Exception:
        return False
    
    bid = float(quotes["bid"].values[0])
    log.info(stock_id +" current bid " + str(bid))
    
    #Check Day here, must stand up MA20
#             data_D = ts.get_k_data(code_id, ktype="D")
#             if not is_prices_above_ema20(bid, data_D):
#                 log.info(code_id + "'s prices under Day MA20")
#                 continue
    

    #Check 30F here
    data_60F = ts.get_k_data(stock_id, ktype="60")
    if not is_prices_above_ema120(bid, data_60F):
        return False
    
    return True

if __name__ == '__main__':
    pass