#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

from datetime import datetime 
from utils.log import log
from utils.constants import GOLDEN_CROSS, DEAD_CROSS

def get_alert_interval(ktype):
    '''
    ktype：string
        数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D    
    '''
    interval = 0
    if "M" in ktype:
        interval = 2 * 60 * 60
    elif "W" in ktype:
        interval = 2 * 60 * 60
    elif "D" in ktype:
        interval = 2 * 60 * 60
    elif "60" in ktype:
        interval = 60 * 60
    elif "30" in ktype:
        interval = 30 * 60
    elif "15" in ktype:
        interval = 15 * 60
    elif "5" in ktype:
        interval = 5 * 60
           
    return interval

def is_alert_needed(stock_entity, ktype, cross_type):
    '''
    we need to check if the alert email is sent recently
    '''
    if "60" in ktype:
        if cross_type == GOLDEN_CROSS:
            last_alert_time = stock_entity.lastGoldenCrossAlert60f
        else:
            last_alert_time = stock_entity.lastDeadCrossAlert60f
    elif "30" in ktype:
        if cross_type == GOLDEN_CROSS:
            last_alert_time = stock_entity.lastGoldenCrossAlert30f
        else:
            last_alert_time = stock_entity.lastDeadCrossAlert30f        
    elif "15" in ktype:
        if cross_type == GOLDEN_CROSS:
            last_alert_time = stock_entity.lastGoldenCrossAlert15f
        else:
            last_alert_time = stock_entity.lastDeadCrossAlert15f   
    elif "5" in ktype:
        if cross_type == GOLDEN_CROSS:
            last_alert_time = stock_entity.lastGoldenCrossAlert05f
        else:
            last_alert_time = stock_entity.lastDeadCrossAlert05f                     
    else:
        log.info("unknown ktype")
        exit(0)
    
    if last_alert_time is None:
        return True
    
    time_delta = datetime.now() - datetime.strptime(last_alert_time, "%Y-%m-%d %H:%M:%S")
    if time_delta.total_seconds() > get_alert_interval(ktype):
        return True
    else:
        return False
    
def is_exchanging_time_now():
    '''
    '''
    td = datetime.now()
    print td
    exchanging_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    if not td.strftime("%A") in exchanging_days:
        log.info("It's not exchanging day today")
        return False
        
    
    if (td.hour == 9 and td.minute >= 25)\
         or (td.hour == 10) \
         or (td.hour == 11 and td.minute <= 30) \
         or (td.hour == 13) \
         or (td.hour == 14):
        return True
    else:
        return False
    print td.hour, td.minute

if __name__ == '__main__':
    is_exchanging_time_now()
