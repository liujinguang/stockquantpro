#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月30日

@author: bob
'''

from libs.indictors.ema import ema

import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import numpy as np

if __name__ == '__main__':
    data = ts.get_k_data('399300', index=True, start="2017-01-01")#, start='2017-01-01'
#     print data
    sma_5 = ema(np.array(data['close']), 5)
    sma_10 = ema(np.array(data['close']), 10)
    sma_20 = ema(np.array(data['close']), 20)
    sma_30 = ema(np.array(data['close']), 30)
    sma_60 = ema(np.array(data['close']), 60)
    sma_120 = ema(np.array(data['close']), 120)
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
#     ax.set_axis_bgcolor('black')
    ax.set_xticks(range(0, len(data['date']), 10))
     
    ax.set_xticklabels(data['date'][::10], rotation=45)
    
    ax.plot(sma_5, label='MA5')
    ax.plot(sma_10, label='MA10', color="#FFFF08")
    ax.plot(sma_20, label='MA20', color="#FF80FF")
    ax.plot(sma_30, label='MA30', color="#00E600")   
    ax.plot(sma_60, label='MA60', color="#02E2F4")
    ax.plot(sma_120, label='MA120', color="#000000")    
    ax.legend(loc='upper left')
     
    mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'],
                     width=0.5, colorup='r', colordown='green',
                     alpha=0.6)
    plt.grid()    
    plt.show()
    