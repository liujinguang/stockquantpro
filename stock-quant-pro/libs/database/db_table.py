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
    isCheckedIn = BoolCol(default=False)
    isIndex = BoolCol(default=False)
    isDeletable = BoolCol(default=False)
    rating = StringCol(default="D")
    lastAlert15f = StringCol(default=None)
    lastAlert30f = StringCol(default=None)
    lastAlert60f = StringCol(default=None)
    

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