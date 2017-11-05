#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月2日

@author: bob
'''

from utils.log import log
from indictors.macd import is_macd_golden_cross_now
from indictors.ema import is_prices_above_ema120, is_prices_above_ema20,\
    is_prices_above_ema_with_period
from utils.emails import send_alert_email

import tushare as ts
import database.db_crud as db_crud
from utils.time_utils import is_exchanging_time_now
from time import sleep

def monitor_indictor_with_30F():
    '''
    '''
    log.info("Start 30F period monitoring...")
    stock_entities = db_crud.get_stock_in_pool(rating="A")
    while True:
#         if not is_exchanging_time_now():
#             log.info("It's not exchanging time now. Sleep 300 seconds")
#             sleep(300)
#             continue
        
        log.info("====New loop start 30F period====")
        for entity in stock_entities:
            is_check_now = False
            email_subject = None
            k_type = None
            
            log.info("Start to check stock " + entity.codeId)
            try:
                quotes = ts.get_realtime_quotes(entity.codeId)
            except Exception:
                continue
            
            bid = float(quotes["bid"].values[0])
            log.info(entity.codeId +" current bid " + str(bid))
            
            #Check Day here, must stand up MA20
#             data_D = ts.get_k_data(code_id, ktype="D")
#             if not is_prices_above_ema20(bid, data_D):
#                 log.info(code_id + "'s prices under Day MA20")
#                 continue
            
            #Check 15F here
            data_15F = ts.get_k_data(entity.codeId, ktype="15")
            if is_macd_golden_cross_now(entity, "15", data_15F) and \
                is_prices_above_ema120(bid, data_15F):
                is_check_now = True
                email_subject = "Quant: 15F golden cross occurs"
                k_type = "15F"
            
            #Check 30F here
            data_30F = ts.get_k_data(entity.codeId, ktype="30")
            if is_macd_golden_cross_now(entity, "30", data_30F) and \
                is_prices_above_ema120(bid, data_30F):
                is_check_now = True
                email_subject = "Quant: 30F golden cross occurs"     
                k_type = "30F"           
                
            #Send email if needs
            if is_check_now:
                send_alert_email(entity, email_subject, "Please check " + entity.codeId + " " + 
                                 entity.name, k_type)    

def monitor_indictor_with_60F():
    '''
    '''
    stock_entities = db_crud.get_stock_in_pool(rating="A")
    while True:
        log.info("====New loop start for 60F period====")
        for entity in stock_entities:
            is_check_now = False
            email_subject = None
            k_type = None
            
            try:
                quotes = ts.get_realtime_quotes(entity.codeId)
            except Exception:
                continue
            
            bid = float(quotes["bid"].values[0])
            log.info(entity.codeId +" current bid " + str(bid))
                      
            #Check 60F here
            data_60F = ts.get_k_data(entity.codeId, ktype="60")
            if not is_prices_above_ema_with_period(entity.codeId, data_60F, bid, 120):
                continue
            
            if is_macd_golden_cross_now(entity.codeId, "60", data_60F):
                is_check_now = True
                email_subject = "Quant 60F: !!!period 60F golden cross occurs!!!"
                k_type = "60F"
            
            #Check 30F here
            data_30F = ts.get_k_data(entity.codeId, ktype="30")
            if is_prices_above_ema120(bid, data_30F) and \
                is_macd_golden_cross_now(entity.codeId, "30", data_30F):
                is_check_now = True
                email_subject = "Quant 60F: period 30F golden cross occurs"     
                k_type = "30F"           
                
            #Send email if needs
            if is_check_now:
                send_alert_email(entity, email_subject, "Please check " + 
                                 entity.codeId + " " + entity.name, k_type)   

if __name__ == '__main__':
    pass