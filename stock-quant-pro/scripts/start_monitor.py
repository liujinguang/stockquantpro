#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

from datetime import datetime
from utils.log import log
from indictors.macd import get_stock_macd, is_macd_golden_cross_now
from utils.emails import send_email
from drawing.drawing_utils import draw_stock_with_multi_periods

import database.db as db
import os
import time

def send_alert_email(code_id, subject, body):
    '''
    Send email to alert
    '''
    log.info("send alert email: " + code_id + " " + subject)
    file_lst = []
    
    fhead = "/home/hadoop/quant/" + datetime.now().strftime("%Y-%m-%d-%H-%M-") + code_id
    
    fname = fhead + "-M-W.png"
    if draw_stock_with_multi_periods(code_id, ("M", "W"), fname):
        file_lst.append(fname)
 
    fname = fhead + "-60F-30F.png"
    if draw_stock_with_multi_periods(code_id, ("60", "30"), fname):
        file_lst.append(fname)
  
    fname = fhead + "-15F-5F.png"
    if draw_stock_with_multi_periods(code_id, ("15", "5"), fname):
        file_lst.append(fname)
    
    send_email("jliu@infinera.com", subject, body, file_lst)  
    
#     for f in file_lst:
#         os.remove(f)    

if __name__ == '__main__':
    
    stock_lst = db.get_stock_list()
    while True:
        log.info("====New loop start====")
        for code_id in stock_lst:
            is_check_now = False
            email_subject = None
            
            #Check 15F here
            if is_macd_golden_cross_now(code_id, "15"):
                is_check_now = True
                email_subject = "Quant: 15F golden cross occurs"
            
            #Check 30F here
            if is_macd_golden_cross_now(code_id, "30"):
                is_check_now = True
                email_subject = "Quant: 30F golden cross occurs"                
                
            #Send email if needs
            if is_check_now:
                send_alert_email(code_id, email_subject, "Please check " + code_id)
            
            
#         time.sleep(60) 
            
    