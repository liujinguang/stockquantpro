#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

from datetime import datetime, timedelta 

def get_start_date(ktype):
    '''
    ktype：string
        数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D    
    '''
#     delta = 0
#     if "M" in ktype:
#         delta = -365 * 5
#     elif "W" in ktype:
#         delta = -365 * 1.5
#     elif "D" in ktype:
#         delta = -240
#     elif "60" in ktype:
#         delta = -45
#     elif "30" in ktype:
#         delta = -21
#     elif "15" in ktype:
#         delta = -14
#     elif "5" in ktype:
#         delta = -5
#  
#     dt = datetime.now() + timedelta(days=delta)
#      
#     return "%d-%02d-%02d" % (dt.year, dt.month, dt.day)
    return None

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

if __name__ == '__main__':
    pass
