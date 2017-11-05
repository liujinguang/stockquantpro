#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

from utils.log import log
import argparse
import monitor.monitoring_utils as monitoring_utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Start to run the monitoring")
    parser.add_argument("--period", choices=["60F", "30F"], 
                        help="Monitor periods 30F or 60F", 
                        default="30F")
    args = parser.parse_args()
    
    if args.period == "30F":
        log.info("Start to monitor 30F period alert")
        monitoring_utils.monitor_indictor_with_30F()
    elif args.period == "60F":
        log.info("Start to monitor 60F period alert")
        monitoring_utils.monitor_indictor_with_60F()
           
    