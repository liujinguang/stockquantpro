#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Nov 3, 2017

@author: hadoop
'''
from database.db_table import StockPoolTbl, StockTbl


def is_id_in_pool(stock_id):
    '''
    '''
    stock_entity = StockPoolTbl.get(id=stock_id)
    
    if stock_entity == None:
        return False
    else:
        return True

def is_id_in_market(stock_id):
    '''
    '''
    stock_entity = StockTbl.get(id=stock_id)
    
    if stock_entity == None:
        return False
    else:
        return True
    
def get_stock_in_pool(stock_id=None):
    '''
    '''
    if stock_id is None:
        return list(StockPoolTbl.select())
    else:
        return list(StockPoolTbl.select(codeId=stock_id))
    
def get_stock_in_market(stock_id=None):
    '''
    '''
    if stock_id is None:
        return list(StockTbl.select())
    else:
        return list(StockTbl.select(codeId=stock_id))    

if __name__ == '__main__':
    pass