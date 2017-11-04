#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Nov 3, 2017

@author: hadoop
'''

import platform

class BaseDb(object):
    '''
    Base class to connect to DBMS
    '''
    def __init__(self, \
                 user='quant', \
                 password='quant123', \
                 host='localhost'):
        self._user = user
        self._password = password
        self._host = host
        self._conn = None
        
    def get_conn(self):
        '''
        Interface for all the child class to implement
        '''
        if self.__class__ is BaseDb:
            raise NotImplementedError

class MysqlDb(BaseDb):
    '''
    define the connection to supervisor_db in mysql
    '''
    def __init__(self):
        BaseDb.__init__(self)
        self._db = 'supervisor_db'
        
    def get_conn(self):
        from sqlobject.mysql import builder
        
        return builder()(user=self._user, \
                 password=self._password, \
                 host=self._host, \
                 db=self._db)

class SqliteDb(BaseDb):
    '''
    define the connection to supervisor_run in sqlite3
    '''
    
    def __init__(self):
        BaseDb.__init__(self)
        self._db = 'supervisor_run'
    
    def get_conn(self):
        from sqlobject.sqlite import builder
        
        return builder()("/var/quant/quant.db")

if __name__ == '__main__':
    pass