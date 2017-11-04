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

from utils.log import log
from database.db_table import StockPoolTbl


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Configure stock")
    
    subparsers = parser.add_subparsers(dest="subparsers_name", 
                                       description="Sub-parser for the stock management")
    
    db_parser = subparsers.add_parser("format", help="Format stock database")
#     db_parser.add_argument("-s", "--start", nargs="?", help="Start to format stock database")
    
    #add list options
    list_parser = subparsers.add_parser("list", help="List stock in the database")
    list_parser.add_argument("-r", "--rating", choices=["A", "B", "C", "D", "ALL"], default="ALL", 
                             help="Rating information")
    list_parser.add_argument("-t", "--type", choices=["pool", "market"], default="pool")
    
    
    #add stock management
    stock_parser = subparsers.add_parser("stock", help="Manage stock pool in the database")
    stock_group = stock_parser.add_mutually_exclusive_group(required=True)
    stock_group.add_argument("-a", "--add", nargs="?", 
                             help="Add one stock into database which needs id, name, index flag")
    stock_group.add_argument("-d", "--delete", nargs="?", 
                             help="Add one stock into database which needs id")
    stock_group.add_argument("-m", "--modify", nargs="?", 
                             help="Add one stock into database which needs id, name, index flag")
    stock_parser.add_argument("-i", "--id", type=int, required=True)
    stock_parser.add_argument("-n", "--name")
    stock_parser.add_argument("--index", type=bool, default=False)
    
    rating_parser = subparsers.add_parser("rating", help="Evaluate the rating of each stock")
    rating_parser.add_argument("-t", "--type", choices=["pool", "market"], default="pool", 
                               help="Choose sources: pool or markets, default pool")    

    args = parser.parse_args()
    print args
    
    if args.subparsers_name == "format":
        print "This operation will format database, please backup the database if it's necessary"
        result = raw_input("Are you sure to cotinue[yes|no]?")
        if result == "yes":
            db_utils.init_database()
            
    elif args.subparsers_name == "rating":
        pass
#         stock_entities = db_crud.get_stock_in_pool()
#         for entity in stock_entities:
#             level = rating.get_stock_rating(entity.codeId)
#             log.info(entity.codeId +"'s rating is " + level)
#             entity.rating = level
            
#         stock_entities = db_crud.get_stock_in_market()
#         for entity in stock_entities:
#             if db_crud.is_id_in_pool(entity.codeId):
#                 continue
#             
#             level = rating.get_stock_rating(entity.codeId)
#             if level == "A":
#                 StockPoolTbl(codeId=entity.codeId, isDeletable=True, name=entity.name, rating="A")
    elif args.subparsers_name == "list":
        pass        
    
            
