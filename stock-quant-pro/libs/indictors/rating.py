#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Nov 3, 2017

@author: hadoop
'''

from utils.log import log
from indictors.ema import ema

import tushare as ts
import numpy as np


def get_stock_rating(code_id):
    '''
    '''
    
    try:
        quotes = ts.get_realtime_quotes(code_id)
    except Exception, e:
        log.info("Error occurs " + e)
        exit(0)
                
    bid = float(quotes["bid"].values[0])
    log.info(code_id +" current bid " + str(bid))
    
    #Check Day here, must stand up MA20
    data_d = ts.get_k_data(code_id, ktype="D")    

    ema20d = ema(np.array(data_d['close']), 20)
    ema30d = ema(np.array(data_d['close']), 30)
    ema60d = ema(np.array(data_d['close']), 60)
    ema120d = ema(np.array(data_d['close']), 120)
    
    log.info("Day MA20 %f, MA60 %f, MA120 %f", ema20d[-1], ema60d[-1], ema120d[-1])
    
    #Check Day here, must stand up MA20
    data_w = ts.get_k_data(code_id, ktype="W")    

    ema5w = ema(np.array(data_w['close']), 5)
    ema10w = ema(np.array(data_w['close']), 10)
    ema20w = ema(np.array(data_w['close']), 20)
    ema30w = ema(np.array(data_w['close']), 30)
    ema60w = ema(np.array(data_w['close']), 60)
    ema120w = ema(np.array(data_w['close']), 120)
   
    log.info("Week MA5 %f, MA10 %f, MA20 %f, MA30 %f, MA60 %f, MA120 %f", 
             ema5w[-1], ema10w[-1], ema20w[-1], ema30w[-1], ema60w[-1], ema120w[-1])

    
    if bid >= ema20d[-1] and ema20d[-1] > ema60d[-1] and ema60d[-1] > ema120d[-1] \
        and ema5w[-1] > ema10w[-1] and ema10w[-1] > ema20w[-1] and ema20w[-1] > ema30w[-1] \
        and ema30w[-1] > ema60w[-1] and ema60w[-1] > ema120w[-1]:
        return "A"
    else:
        return "D"               


if __name__ == '__main__':
    print get_stock_rating("600320")