#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月30日

@author: bob
'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import numpy as np
import tushare as ts
import talib as tl

def _ewma(N, m, expma, prices):
    '''
        指数平滑均线函数.
        以prices计算，可以选择收盘、开盘价等价格，period为时间周期，
    m用于计算平滑系数a=m/(period+1)，exp_ma为前一日值指数评价值
    '''
    a = m / (N + 1.0)
    return a * prices + (1 - a) * expma

def ma(prices, period, N=60, m=2.0):
#     expma = pd.ewma(prices, span=period)
#     ema = tl.EMA(prices, period)
    
#     return _ewma(N, m, ema, prices)
    return tl.EMA(prices, period)

if __name__ == '__main__':
    data = ts.get_k_data('399300', index=True)
    sma_5 = ma(np.array(data['close']), 5)
    sma_10 = ma(np.array(data['close']), 10)
    sma_20 = ma(np.array(data['close']), 20)
    sma_30 = ma(np.array(data['close']), 30)
    sma_60 = ma(np.array(data['close']), 60)    
     
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xticks(range(0, len(data['date']), 10))
     
    ax.set_xticklabels(data['date'][::10], rotation=45)
    ax.plot(sma_10, label='MA5')
    ax.plot(sma_10, label='MA10')
    ax.plot(sma_20, label='MA20')
    ax.plot(sma_30, label='MA30')   
    ax.plot(sma_60, label='MA60')  
    ax.legend(loc='upper left')
     
    mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'],
                     width=0.5, colorup='r', colordown='green',
                     alpha=0.6)
    plt.grid()    
    plt.show()