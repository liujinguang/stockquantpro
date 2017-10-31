#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''


from utils.log import log
from indictors.macd import get_stock_macd 
from utils.emails import send_email
from drawing.drawing_utils import draw_stock_with_multi_periods

import database.db as db
import os
import time

def send_alert_email(code_id, subject, body):
    log.info("send alert email: " + code_id + " " + subject)
    file_lst = []
    
    fname = "/home/hadoop/" + code_id + "-month-week" + ".png"
    draw_stock_with_multi_periods(code_id, ("M", "W"), fname)
    file_lst.append(fname)
 
    fname = "/home/hadoop/" + code_id + "-60F-30F" + ".png"
    draw_stock_with_multi_periods(code_id, ("60", "30"), fname)
    file_lst.append(fname)
  
    fname = "/home/hadoop/" + code_id + "-15F-5F" + ".png"
    draw_stock_with_multi_periods(code_id, ("15", "5"), fname)
    file_lst.append(fname)
    
    send_email("jliu@infinera.com", subject, body, file_lst)  
    
    for f in file_lst:
        os.remove(f)    

if __name__ == '__main__':
    
    stock_lst = db.get_stock_list()
    while True:
        for code_id in stock_lst:
            log.info("Start to check " + code_id + " 15F MACD")
            ktype = "15"
            diff15, dea15, bar15 = get_stock_macd(code_id, ktype, db.is_index(code_id))
            
            print bar15.values

            if bar15.values[-2] < 0 and bar15.values[-1] >= 0 and db.is_alert_needed(code_id, ktype):
                send_alert_email(code_id, "Quant: 15F occurs", "Please check " + code_id)
            
            send_alert_email(code_id, "Quant: 15F occurs", "Please check " + code_id)
            
            log.info("Start to check " + code_id + " 30F MACD")    
            ktype = "30"
            diff30, dea30, bar30 = get_stock_macd(code_id, ktype, db.is_index(code_id))
            print bar30.values
            if bar30.values[-2] < 0 and bar30.values[-1] >= 0 and db.is_alert_needed(code_id, ktype):
                send_alert_email(code_id, "Quant: 30F occurs", "Please check " + code_id)  
                
#         time.sleep(60) 
        break         
            
    