#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2018年2月5日

@author: HP
'''

from jaqs.data import DataApi

from config.config_path import get_data_config_path, get_trader_config_path

import jaqs.util as jutil


def get_market_stocks():
    '''
            提供了全部的证券标的基本信息
    '''
    data_config = jutil.read_json(get_data_config_path())
    trade_config = jutil.read_json(get_trader_config_path())
    
    data_api = DataApi(addr='tcp://data.tushare.org:8910')
    
    df, msg = data_api.login(data_config["remote.data.username"],
                             data_config["remote.data.password"])
    
    print(df, msg)
    
    # inst_type = 1   表示股票
    # status = 1      表示股票正常交易，未退市
    # market = SH,SZ  取上海和深圳的股票
    df, msg = data_api.query("jz.instrumentInfo",
                             filter="inst_type=1&status=1&market=SH,SZ",
                             fields="market,symbol,list_date,status",
                             data_format='pandas')
    print(df)
    print(len(df))
    print(len(df[df['market'] == 'SZ']))
    print(len(df[df['market'] == 'SH']))
    
    return df


def stock_issuing_stats(df):
    '''
            按照月度统计，看看股票发行数量的分布情况
    '''
    list_date = df['list_date'].astype(int)
    
    ser_year = list_date // 10000
    year_month = list_date // 100
    
    gp = df.groupby(by=year_month)


if __name__ == '__main__':
    pass
