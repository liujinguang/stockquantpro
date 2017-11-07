#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Nov 4, 2017

@author: bob
'''
# from database.db_crud import db_crud
from utils.log import log

import numpy as np
import tushare as ts
import os
import database.db_crud as db_crud
import argparse
import time


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
    
def is_macd_golen_cross_now_for_selection(stock_id, ktype):
    '''
    '''
    try:
        quotes = ts.get_realtime_quotes(stock_id)
    except Exception:
        return False
    
    bid = float(quotes["bid"].values[0])
    log.info(stock_id +" current bid " + str(bid))
    
    #Check 30F here
    data_d = ts.get_k_data(stock_id, ktype=ktype)
    
    #if checks the day K, it must be above the ema120
    if ktype == "D" and not is_prices_above_ema120(bid, data_d):
        return False
    
    diff, dea, bar = get_stock_macd(stock_id, ktype, data=data_d)
    if bar.values[-1] >= 0 and bar.values[-2] < 0:
        return True
    else:
        return False
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Select stocks from the database")
    subparsers = parser.add_subparsers(dest="subparsers_name", 
                                       description="Sub-parser for the stock selection")
    
    reset_parser = subparsers.add_parser("reset", help="Reset the observed flag for all stocks")
        
    select_parser = subparsers.add_parser("select", help="Select stock from the database by policy")
    select_group = select_parser.add_mutually_exclusive_group()
    select_group.add_argument("--period", nargs="?", 
                              choices=["W", "D"], 
                              default="D",
                              help="Period used, default is D")
    select_group.add_argument("--policy", nargs="?", 
                              choices=["ma", "macd"], 
                              default="macd",
                              help="Policy used, default is macd")
    args = parser.parse_args()
    
    if args.subparsers_name == "reset":
        db_crud.reset_observed_config()
    elif args.subparsers_name == "select":
        stock_entities = db_crud.get_stock_in_pool()
        for entity in stock_entities:
            if args.policy == "macd":
                log.info("Start to check stock " + entity.codeId)
                if is_macd_golen_cross_now_for_selection(entity.codeId, ktype=args.period):
                    log.info("MACD golden cross")
                    entity.isObserved = True
                    
                log.info("Done!")
                
                time.sleep(2)
    
#     stock_entities = db_crud.get_stock_in_market()
#      
#     for entity in stock_entities:
#         code_id = entity.codeId
#         if is_day_period_golen_cross(code_id):
#             log.info("Day golden cross: " + code_id)
#             entity.isObserved = True
    
#     code_id = "300450"
#     fname = get_charts_root_directory() + os.sep + code_id + ".png"
#     draw_stock_with_candlestick_macd(code_id, ("W", "D", "30", "15"), fname)
    