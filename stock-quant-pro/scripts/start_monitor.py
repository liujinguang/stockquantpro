#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

from datetime import datetime
from utils.log import log
from indictors.macd import get_stock_macd, is_macd_golden_cross_now
from indictors.ema import is_prices_above_ema120
from utils.emails import send_email
from drawing.drawing_utils import draw_stock_with_multi_periods2

import database.db as db
import os
import time
import tushare as ts
import platform

def send_alert_email(code_id, subject, body):
    '''
    Send email to alert
    '''
    log.info("send alert email: " + code_id + " " + subject)
    file_lst = []
    
    if platform.system() == "Linux":
        fhead = "/home/hadoop/quant/" + datetime.now().strftime("%Y-%m-%d-%H-%M-") + code_id
    else:
        fhead = 'd:\\quant\\result\\' + datetime.now().strftime("%Y-%m-%d-%H-%M-") + code_id
    
#     fname = fhead + "-W-D.png"
#     if draw_stock_with_multi_periods(code_id, ("W", "D"), fname):
#         file_lst.append(fname)
#  
#     fname = fhead + "-60F-30F.png"
#     if draw_stock_with_multi_periods(code_id, ("60", "30"), fname):
#         file_lst.append(fname)
#   
#     fname = fhead + "-15F-5F.png"
#     if draw_stock_with_multi_periods(code_id, ("15", "5"), fname):
#         file_lst.append(fname)
    fname = fhead + "-all-periods.png"
    if draw_stock_with_multi_periods2(code_id, ("W", "D", "60", "30", "15", "5"), fname):
        file_lst.append(fname)
    
#     send_email("jliu@infinera.com", code_id + " " + subject, body, file_lst)  
    
#     for f in file_lst:
#         os.remove(f)    

if __name__ == '__main__':
    
    start_time = datetime.now()
    
    stock_lst = db.get_stock_list()
    while True:
        log.info("====New loop start====")
        for code_id in stock_lst:
            is_check_now = False
            email_subject = None
            
            quotes = ts.get_realtime_quotes(code_id)
            bid = float(quotes["bid"].values[0])
            log.info(code_id +" current bid " + str(bid))
            
            #Check 15F here
            data_15F = ts.get_k_data(code_id, ktype="15")
            if is_macd_golden_cross_now(code_id, "15", data_15F) and is_prices_above_ema120(bid, data_15F):
                is_check_now = True
                email_subject = "Quant: 15F golden cross occurs"
            
            #Check 30F here
            data_30F = ts.get_k_data(code_id, ktype="30")
            if is_macd_golden_cross_now(code_id, "30", data_30F) and is_prices_above_ema120(bid, data_30F):
                is_check_now = True
                email_subject = "Quant: 30F golden cross occurs"                
                
            #Send email if needs
            if is_check_now:
                send_alert_email(code_id, email_subject, "Please check " + code_id + " " + 
                                 db.get_stock_name(code_id))
            
#         if (datetime.now() - start_time).total_seconds() > 15 * 60:
#             log.info("Market stop now.")
#             break    
#         time.sleep(60) 
            
    