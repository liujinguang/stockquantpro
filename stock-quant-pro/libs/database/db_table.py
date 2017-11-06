#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Nov 3, 2017

@author: hadoop
'''

from db_driver import SqliteDb

from sqlobject.styles import MixedCaseUnderscoreStyle

from sqlobject.col import StringCol, IntCol, ForeignKey, DateTimeCol, BoolCol
from sqlobject.joins import MultipleJoin, RelatedJoin
from sqlobject import SQLObject
from isort.settings import default

conn_dbms = SqliteDb().get_conn()
conn_dbms.text_factory = str

class SQLObjectBase(SQLObject):
    _connection = conn_dbms
    _fromDatabase = True
    _connection.debug = False

class StockPoolTbl(SQLObjectBase):
    '''
    Stock pool table
    '''
    class sqlmeta:
        style = MixedCaseUnderscoreStyle()
        idName = "id"
        table = 'stock_pool_tbl'
        cachedValues = False

    codeId = StringCol()
    name = StringCol(alternateID=True, length=16)
    isIndex = BoolCol(default=False)
    isObserved = BoolCol(default=False)
    isMonitored = BoolCol(default=False)
    rating = StringCol(default="D")
    policy = StringCol(default="ma")
    isGoldenCrossAlert05f = BoolCol(default=False)
    isGoldenCrossAlert15f = BoolCol(default=False)
    isGoldenCrossAlert30f = BoolCol(default=False)
    isGoldenCrossAlert60f = BoolCol(default=False)
    isDeadCrossAlert05f = BoolCol(default=False)
    isDeadCrossAlert15f = BoolCol(default=False)
    isDeadCrossAlert30f = BoolCol(default=False)
    isDeadCrossAlert60f = BoolCol(default=False)    
    lastGoldenCrossAlert05f = StringCol(default=None)
    lastGoldenCrossAlert15f = StringCol(default=None)
    lastGoldenCrossAlert30f = StringCol(default=None)
    lastGoldenCrossAlert60f = StringCol(default=None)
    lastDeadCrossAlert05f = StringCol(default=None)
    lastDeadCrossAlert15f = StringCol(default=None)
    lastDeadCrossAlert30f = StringCol(default=None)
    lastDeadCrossAlert60f = StringCol(default=None)    
    

class StockTbl(SQLObjectBase):
    '''
    Stock pool table
    '''
    class sqlmeta:
        style = MixedCaseUnderscoreStyle()
        idName = "id"
        table = 'stock_tbl'
        cachedValues = False
    
    codeId = StringCol()    
    name = StringCol(alternateID=True, length=16)
    isObserved = BoolCol(default=False)
    

    
    
if __name__ == '__main__':
    pass