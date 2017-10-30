#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月30日

@author: bob
'''

from libs.indictors.ema import ema
from libs.indictors.macd import macd

import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import numpy as np

def draw_candle_stick(ax, data):
#     if start is not None:
#         data = ts.get_k_data(code_id, ktype=ktype, index=True, start=start)
#     else:
#         data = ts.get_k_data(code_id, ktype=ktype, index=True, start='2017-01-01')

    ema5 = ema(np.array(data['close']), 5)
    ema10 = ema(np.array(data['close']), 10)
    ema20 = ema(np.array(data['close']), 20)
    ema30 = ema(np.array(data['close']), 30)
    ema60 = ema(np.array(data['close']), 60)
    ema120 = ema(np.array(data['close']), 120)
    
    #make these tick labels invisible
    plt.setp(ax.get_xticklabels(), visible=False)
    
#     ax.set_xticks(range(0, len(data['date']), 10))
      
#     ax.set_xticklabels(data['date'][::10], rotation=45)
    
    
    ax.plot(ema5, label='MA5')
    ax.plot(ema10, label='MA10', color="#FFFF08")
    ax.plot(ema20, label='MA20', color="#FF80FF")
    ax.plot(ema30, label='MA30', color="#00E600")   
    ax.plot(ema60, label='MA60', color="#02E2F4")
    ax.plot(ema120, label='MA120', color="#000000")    
    ax.legend(loc='upper left')
#     ax.set_title("KAAA")
     
    mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'],
                     width=0.5, colorup='r', colordown='green',
                     alpha=0.6)
#     plt.grid()    
#     plt.show()


def draw_volumes(ax, data):
    ema5 = ema(np.array(data['volume']), 5)
    ema10 = ema(np.array(data['volume']), 10)
    #make these tick labels invisible
    plt.setp(ax.get_xticklabels(), visible=False)
    
    ax.plot(ema5, label='MA5')
    ax.plot(ema10, label='MA10', color="#FFFF08")
    ax.bar(data['date'], data['volume'], width=0.3, color='red', label="Volume")
    

def draw_macd(ax, data):
    diff, dea, _macd = macd(data['close'].values)

    ax.set_xticks(range(0, len(data['date']), 10))
       
    ax.set_xticklabels(data['date'][::10], rotation=45)
    
    ax.plot(data['date'], diff, label='DIFF')
    ax.plot(data['date'], dea, label='DEA')
    ax.legend(loc='upper left')
    
    ax.bar(data['date'], _macd, width=0.3, color='red', label="MACD")

def draw_stock_with_multi_periods(code_id, periods):
#     if start is not None:
#         data = ts.get_k_data(code_id, ktype=ktype, index=True, start=start)
#     else:

    #weekly TA
    w_data = ts.get_k_data(code_id, ktype="W", index=True, start='2015-6-30')    
    fig = plt.figure(figsize=(18,5))
    w_ax_k = fig.add_subplot(3, 2, 1)
    w_ax_k.set_title("Week Technical Analyzation")
    draw_candle_stick(w_ax_k, w_data)
    
    w_ax_volume = fig.add_subplot(3, 2, 3, sharex=w_ax_k)
    draw_volumes(w_ax_volume, w_data)
    
    w_ax_macd = fig.add_subplot(3, 2, 5, sharex=w_ax_k)
    draw_macd(w_ax_macd, w_data)

    d_data = ts.get_k_data(code_id, index=True, start='2017-05-01')    
#     fig = plt.figure()
    d_ax_k = fig.add_subplot(3, 2, 2)
    d_ax_k.set_title("Day Technical Analyzation")
    draw_candle_stick(d_ax_k, d_data)
    
    d_ax_volume = fig.add_subplot(3, 2, 4, sharex=d_ax_k)
    draw_volumes(d_ax_volume, d_data)
    
    d_ax_macd = fig.add_subplot(3, 2, 6, sharex=d_ax_k)
    draw_macd(d_ax_macd, d_data)

    plt.grid()
    plt.savefig(code_id + ".png")    
#     plt.show()

if __name__ == '__main__':
    draw_stock_with_multi_periods("399300", None)

