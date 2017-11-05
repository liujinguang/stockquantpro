#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Nov 3, 2017

@author: hadoop
'''

import argparse

import database.db_utils as db_utils
import database.db_crud as db_crud
import indictors.rating as rating
import policies.ma_policy as ma_policy

from utils.log import log
from database.db_table import StockPoolTbl
from drawing.drawing_utils import get_charts_root_dir,\
    draw_stock_with_candlestick_macd


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Configure stock")
    
    subparsers = parser.add_subparsers(dest="subparsers_name", 
                                       description="Sub-parser for the stock management")
    
    db_parser = subparsers.add_parser("format", help="Format stock database")
#     db_parser.add_argument("-s", "--start", nargs="?", help="Start to format stock database")
    
    #add list options
    list_parser = subparsers.add_parser("list", help="List stock in the database")
    list_group = list_parser.add_mutually_exclusive_group(required=False)
    list_group.add_argument("-r", "--rating", 
                             choices=["A", "B", "C", "D", "ALL"], 
                             default="ALL", 
                             help="Rating information, default is ALL")
    list_group.add_argument("-t", "--type", 
                             choices=["pool", "market"], 
                             default="pool",
                             help="Resource type, default is pool")
    list_group.add_argument("-i", "--id", help="Stock ID")
    
    drawing_parser = subparsers.add_parser("draw", 
                                           help="Draw stock charts for stocks in pool")
    draw_group = drawing_parser.add_mutually_exclusive_group(required=False)
    draw_group.add_argument("-r", "--rating", 
                             choices=["A", "B", "C", "D", "ALL"], 
                             default="A", 
                             help="Rating information, default is A")
    draw_group.add_argument("-i", "--id", nargs="?", help="Stock ID")
    drawing_parser.add_argument("-p", "--period", 
                            choices=[1, 2, 3, 4, 5], 
                            type=int, 
                            help="Periods used: \n1 includes W, D; " + \
                            "2: includes W, D, 30F, 15F; " + \
                            "3: includes W, D, 60F, 30F, 15F, 5F. " + \
                            "4: includes D, 60F, 30F, 15F"
                            "5: includes 30F, 15F. Default is 2.",
                            default=2)
    drawing_parser.add_argument("--policy", 
                            choices=["none", "ma_30f", "ma_60f"], 
                            help="Policy: default is none",
                            default="none")    
    
    #add stock management
    stock_parser = subparsers.add_parser("stock", help="Manage stock pool in the database")
    stock_group = stock_parser.add_mutually_exclusive_group(required=True)
    stock_group.add_argument("-a", "--add", nargs="?", 
                             help="Add one stock into database which needs id, name, index flag")
    stock_group.add_argument("-d", "--delete", nargs="?", 
                             help="Add one stock into database which needs id")
    stock_group.add_argument("-m", "--modify", nargs="?", 
                             help="Add one stock into database which needs id, name, index flag")
    stock_parser.add_argument("-i", "--id", required=True)
    stock_parser.add_argument("-n", "--name")
    stock_parser.add_argument("--index", choices=["True", "False"], default="False")
    stock_parser.add_argument("-c", "--check-in", choices=["True", "False"], default="False")
    
    rating_parser = subparsers.add_parser("rating", help="Evaluate the rating of each stock")
    rating_parser.add_argument("-t", "--type", choices=["pool", "market"], default="pool", 
                               help="Choose sources: pool or markets, default pool")    

    args = parser.parse_args()
    
    if args.subparsers_name == "format":
        print "This operation will format database, please backup the database if it's necessary"
        result = raw_input("Are you sure to cotinue[yes|no]?")
        if result == "yes":
            db_utils.init_database()
            
    elif args.subparsers_name == "rating":
        log.info("This operation will rate the stock again.")
        log.info("Old configuration will be lost.")
        log.info("Are you sure to continue [yes|no]?")
        result = raw_input()        
        if result != "yes":
            exit(0)
            
        stock_entities = db_crud.get_stock_in_pool()
        for entity in stock_entities:
            level = rating.get_stock_rating(entity.codeId)
            log.info(entity.codeId +"'s rating is " + level)
            entity.rating = level
             
        stock_entities = db_crud.get_stock_in_market()
        for entity in stock_entities:
            if db_crud.is_id_in_pool(entity.codeId):
                continue
             
            level = rating.get_stock_rating(entity.codeId)
            log.info("Stock " + entity.codeId + "'s level is " + level)
            if level == "A":
                StockPoolTbl(codeId=entity.codeId, isDeletable=True, name=entity.name, rating="A")
                
    elif args.subparsers_name == "list":
        if args.type == "pool":
            log.info("%-10s%-12s%-7s%-7s%-10s%-6s%-22s%-22s%-22s", 
                     "股票编码".decode('utf-8').encode('gbk'), 
                     "股票名称".decode('utf-8').encode('gbk'), 
                     "买入?".decode('utf-8').encode('gbk'), 
                     "指数?".decode('utf-8').encode('gbk'), 
                     "可删除?".decode('utf-8').encode('gbk'), 
                     "评级".decode('utf-8').encode('gbk'), 
                     "15F告警时间".decode('utf-8').encode('gbk'), 
                     "30F告警时间".decode('utf-8').encode('gbk'), 
                     "60F告警时间".decode('utf-8').encode('gbk') )
            
            if args.id is not None:
                entity = db_crud.get_stock_in_pool(stock_id=args.id)
                if entity is not None:
                    log.info("%-10s%-12s%-7s%-7s%-10s%-6s%-22s%-22s%-22s", 
                             entity.codeId,
                             entity.name.decode('utf-8').encode('gbk'),
                             "Yes" if entity.isCheckedIn else "No",
                             "Yes" if entity.isIndex  else "No",
                             "Yes" if entity.isDeletable  else "No",
                             entity.rating, 
                             entity.lastAlert15f,
                             entity.lastAlert30f,
                             entity.lastAlert60f)   
            else:
                count = 0
                stock_entities = db_crud.get_stock_in_pool()
                for entity in stock_entities:
                    if args.rating == "ALL" or entity.rating == args.rating:
                        count += 1
                        log.info("%-10s%-12s%-7s%-7s%-10s%-6s%-22s%-22s%-22s", 
                                 entity.codeId,
                                 entity.name.decode('utf-8').encode('gbk'),
                                 "Yes" if entity.isCheckedIn else "No",
                                 "Yes" if entity.isIndex  else "No",
                                 "Yes" if entity.isDeletable  else "No",
                                 entity.rating, 
                                 entity.lastAlert15f,
                                 entity.lastAlert30f,
                                 entity.lastAlert60f)    
                log.info("=" * 120) 
                log.info("Total stocks: %d", count)                             

    elif args.subparsers_name == "stock":
        stock_id = args.id
        if args.delete is not None:
            db_crud.delete_stock_in_pool(stock_id)
        elif args.modify is not None:
            stock_entity = db_crud.get_stock_in_pool(stock_id)    
            if stock_entity is None:
                log.info("Stock " + stock_id + " doesn't exist")
                exit(1)

            if args.check_in == "True":
                stock_entity.isCheckedIn = True
            else:
                stock_entity.isCheckedIn = False
            
            if args.index == "True":
                stock_entity.isIndex = True
            else:
                stock_entity.isIndex = False
    elif args.subparsers_name == "draw":
        if args.period == 1:
            periods = ("W", "D")
        elif args.period == 2:
            periods = ("W", "D", "30", "15")
        elif args.period == 3:
            periods = ("W", "D", "60", "30", "15", "5")
        elif args.period == 4:
            periods = ("D", "60", "30", "15")            
        else:
            periods = ("30", "15")
            
        rdir = get_charts_root_dir("-drawing")
        if args.id is not None:
            stock_id = args.id
            stock_entity = db_crud.get_stock_in_pool(stock_id=stock_id)
            if stock_entity is None:
                stock_entity = db_crud.get_stock_in_market(stock_id=stock_id)
                if stock_entity is None:
                    log.info("Invlid stock ID: " + stock_id)
                    exit(0)
                     
            fname = rdir + stock_id + "-" + \
                    stock_entity.name.decode('utf-8').encode('gbk') + ".png"
            draw_stock_with_candlestick_macd(stock_id, periods, fname, 
                                             index=stock_entity.isIndex)
            log.info("!!!Done!!!")
            log.info("Please check the directory " + rdir)
             
        else:
            count = 0
            stock_entities = db_crud.get_stock_in_pool()
            for entity in stock_entities:
                if args.rating == "ALL" or entity.rating == args.rating:
                    if args.policy == "ma_30f" and not ma_policy.is_ma_30f_satisfied(entity.codeId):
                        continue
                    
                    if args.policy == "ma_60f" and not ma_policy.is_ma_60f_satisfied(entity.codeId):
                        continue
                                        
                    count += 1            
                    
                    stock_id = entity.codeId
                    log.info("Start to draw chart for " + stock_id)
                    
                    #generate chart name
                    fname = rdir + stock_id + "-" + \
                            entity.name.decode('utf-8').encode('gbk')                            
                    for p in periods:
                        fname = fname + "-" + p
                    fname = fname + ".png"
                    
                    
                    draw_stock_with_candlestick_macd(stock_id, periods, fname, index=False)
                    log.info("Done!")
                    
            log.info("!!!Done!!!")
            log.info("Please check the directory " + rdir)            
    else:
        parser.print_help()    
        print args               
    
            
