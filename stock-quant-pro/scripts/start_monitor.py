#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

# from monitor.monitoring_utils import monitor_indictor_with_30F, monitor_indictor_with_30F

from datetime import datetime
from utils.log import log
from indictors.macd import get_stock_macd, is_macd_golden_cross_now
from indictors.ema import is_prices_above_ema120, is_prices_above_ema20
from utils.emails import send_email
from drawing.drawing_utils import draw_stock_with_multi_periods2

import database.db as db
import os
import time
import tushare as ts
import platform
import socket
import argparse

import monitor.monitoring_utils as monitoring_utils


# def send_alert_email(code_id, subject, body, k_type):
#     '''
#     Send email to alert
#     '''
#     log.info("send alert email: " + code_id + " " + subject)
#     file_lst = []
#     
#     if platform.system() == "Linux":
#         fhead = "/home/hadoop/quant/2017-11-02/" + code_id + "-"+ k_type + "-" + datetime.now().strftime("%Y-%m-%d-%H-%M-")
#     else:
#         fhead = 'd:\\quant\\result\\' + code_id + "-" + datetime.now().strftime("%Y-%m-%d-%H-%M-")
#     
# #     fname = fhead + "-W-D.png"
# #     if draw_stock_with_multi_periods(code_id, ("W", "D"), fname):
# #         file_lst.append(fname)
# #  
# #     fname = fhead + "-60F-30F.png"
# #     if draw_stock_with_multi_periods(code_id, ("60", "30"), fname):
# #         file_lst.append(fname)
# #   
# #     fname = fhead + "-15F-5F.png"
# #     if draw_stock_with_multi_periods(code_id, ("15", "5"), fname):
# #         file_lst.append(fname)
#     fname = fhead + "-all-periods.png"
#     if draw_stock_with_multi_periods2(code_id, ("W", "D", "60", "30", "15", "5"), fname):
#         file_lst.append(fname)
#     
#     send_email("jliu@infinera.com", code_id + " " + subject, body)  
    
#     for f in file_lst:
#         os.remove(f)    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Start to run the monitoring")
    parser.add_argument("--period", choices=["60F", "30F"], help="Monitor periods 30F and 15F", default=None)
    args = parser.parse_args()
    
    if args.period == "30F":
        monitoring_utils.monitor_indictor_with_30F()
    elif args.period == "60F":
        monitoring_utils.monitor_indictor_with_60F()
#     if args.thirteen == "30F":
#         print "30F&15F"
# #     print args
#     start_time = datetime.now()
#     
#     stock_lst = db.get_stock_list()
#     while True:
#         log.info("====New loop start====")
#         for code_id in stock_lst:
#             is_check_now = False
#             email_subject = None
#             k_type = None
#             
#             try:
#                 quotes = ts.get_realtime_quotes(code_id)
#             except Exception:
#                 continue
#             
#             bid = float(quotes["bid"].values[0])
#             log.info(code_id +" current bid " + str(bid))
#             
#             #Check Day here, must stand up MA20
#             data_D = ts.get_k_data(code_id, ktype="D")
#             if not is_prices_above_ema20(bid, data_D):
#                 log.info(code_id + "'s prices under Day MA20")
#                 continue
#             
#             #Check 15F here
#             data_15F = ts.get_k_data(code_id, ktype="15")
#             if is_macd_golden_cross_now(code_id, "15", data_15F) and is_prices_above_ema120(bid, data_15F):
#                 is_check_now = True
#                 email_subject = "Quant: 15F golden cross occurs"
#                 k_type = "15F"
#             
#             #Check 30F here
#             data_30F = ts.get_k_data(code_id, ktype="30")
#             if is_macd_golden_cross_now(code_id, "30", data_30F) and is_prices_above_ema120(bid, data_30F):
#                 is_check_now = True
#                 email_subject = "Quant: 30F golden cross occurs"     
#                 k_type = "30F"           
#                 
#             #Send email if needs
#             if is_check_now:
#                 send_alert_email(code_id, email_subject, "Please check " + code_id + " " + 
#                                  db.get_stock_name(code_id), k_type)
            
#         if (datetime.now() - start_time).total_seconds() > 15 * 60:
#             log.info("Market stop now.")
#             break    
#         time.sleep(60) 
            
    