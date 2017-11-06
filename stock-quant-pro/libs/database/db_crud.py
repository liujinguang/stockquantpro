#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Nov 3, 2017

@author: hadoop
'''
from database.db_table import StockPoolTbl, StockTbl
from utils.log import log
from datetime import datetime


def is_id_in_pool(stock_id):
    '''
    '''
    stock_entity = get_stock_in_pool(stock_id=stock_id)
    
    if stock_entity is None:
        return False
    else:
        return True
    
def delete_stock_in_pool(stock_id):
    stock_entity = get_stock_in_pool(stock_id)
    
    if stock_entity == None:
        log.info("Stock " + stock_id + " doesn't exist")
        return False
    elif not stock_entity.isDeletable:
        log.info("Stock " + stock_id + " is not deletable")
        return False
    else:
        StockPoolTbl.delete(stock_entity.id)
        log.info("Stock " + stock_id + " is deleted")
        return True    

def is_id_in_market(stock_id):
    '''
    '''
    stock_entity = StockTbl.get(id=stock_id)
    
    if stock_entity == None:
        return False
    else:
        return True
    
def reset_alert_config(stock_id=None):
    '''
    reset alert configuration of the stock
    '''
    if stock_id is not None:
        stock_entity = get_stock_in_pool(stock_id)
        if stock_entity is None:
            log.info("Stock " + stock_id + " doesn't exist!")
            
            return
        
        stock_entity.isMonitored = False
        stock_entity.isGoldenCrossAlert05f = False
        stock_entity.isGoldenCrossAlert15f = False
        stock_entity.isGoldenCrossAlert30f = False
        stock_entity.isGoldenCrossAlert60f = False
        stock_entity.isDeadCrossAlert05f = False
        stock_entity.isDeadCrossAlert15f = False
        stock_entity.isDeadCrossAlert30f = False
        stock_entity.isDeadCrossAlert60f = False
    else:
        stock_entities = get_stock_in_pool()
        
        for stock_entity in stock_entities:
            if stock_entity.isMonitored is True:
                stock_entity.isMonitored = False
                stock_entity.isGoldenCrossAlert05f = False
                stock_entity.isGoldenCrossAlert15f = False
                stock_entity.isGoldenCrossAlert30f = False
                stock_entity.isGoldenCrossAlert60f = False
                stock_entity.isDeadCrossAlert05f = False
                stock_entity.isDeadCrossAlert15f = False
                stock_entity.isDeadCrossAlert30f = False
                stock_entity.isDeadCrossAlert60f = False                
        
    
def get_stock_in_pool(stock_id=None, rating=None):
    '''
    '''
    
    if stock_id is not None:
        lst = list(StockPoolTbl.selectBy(codeId=stock_id))
        if len(lst) != 0:
            return lst[0]
        else:
            return None
    else:
        if rating is None:
            return list(StockPoolTbl.select())
        else:
            return list(StockPoolTbl.selectBy(rating=rating))
    
def get_stock_in_market(stock_id=None):
    '''
    '''
    if stock_id is not None:
        lst = list(StockTbl.selectBy(codeId=stock_id))
        if len(lst) != 0:
            return lst[0]
        else:
            return None
    else:
        return list(StockTbl.select())

def update_alert_time(stock_entity,ktype):
    '''
    update alert time
    '''
    log.info("update alert time for " + stock_entity.codeId + " " + ktype)
    if "15" in ktype:
        stock_entity.lastAlert15f = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif "30" in ktype:
        stock_entity.lastAlert30f = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif "60" in ktype:
        stock_entity.lastAlert60f = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    else:
        log.info("Unknown ktype for " + stock_entity.codeId + " " + ktype)       



if __name__ == '__main__':
    pass