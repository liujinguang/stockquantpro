#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

from datetime import datetime
from utils.time_utils import get_alert_interval

stock_pool = {
    "002352" : {"name":"顺风控股", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
    "002294" : {"name":"信立泰", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600887" : {"name":"伊利股份", "index":False, "In":False, "15F_Falert_time":None, "30F_alert_time":None},
    }


def get_stock_pool():
    return stock_pool

def get_stock_list():
    return stock_pool.keys()

def is_index(code_id):
    return stock_pool[code_id]["index"]
    
def update_alert_time(code_id, ktype):
    '''
    update alert time
    '''
    if "15" in ktype:
        stock_pool[code_id]["15F_Falert_time"] = datetime.now()
    else:
        stock_pool[code_id]["30F_Falert_time"] = datetime.now()

def get_alert_time(code_id, ktype):
    '''
    '''
    if "15" in ktype:
        return stock_pool[code_id]["15F_Falert_time"]
    else:
        return stock_pool[code_id]["30F_Falert_time"]
    
def is_alert_needed(code_id, ktype):
    '''
    '''
    if "15" in ktype:
        last_alert_time = stock_pool[code_id]["15F_Falert_time"]
    else:
        last_alert_time = stock_pool[code_id]["30F_Falert_time"] = datetime.now()    

    interval_time = datetime.now() - last_alert_time
    if interval_time.total_seconds() - get_alert_interval(ktype) > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    pass