#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月30日

@author: bob
'''

from indictors.ema import ema
from indictors.macd import macd
from utils.log import log
from utils.time_utils import get_start_date

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

def draw_stock_with_multi_periods(code_id, periods, fname, index=False):
#     if start is not None:
#         data = ts.get_k_data(code_id, ktype=ktype, index=True, start=start)
#     else:
    if len(periods) == 0:
        log.error("periods parameter doesn't have any valid values")
        return

    fig = plt.figure(figsize=(40,20))
#     fig.set_title(code_id)
    num = len(periods)
    
    #create index
    indexs = np.arange(1, 3*num+1).reshape(3, num)
#     print aa
#     for i in xrange(num):
#         print aa[0][i], aa[1][i], aa[2][i]    
    
    for i in xrange(num):
        ktype = periods[i]
        start = get_start_date(ktype)
        print start, ktype
        data = ts.get_k_data(code_id, ktype=ktype, index=index, start=start)    
        data = data[data.date >= start]
        ax_k = fig.add_subplot(3, num, indexs[0][i])
        ax_k.set_title(get_chart_title(ktype))
        draw_candle_stick(ax_k, data)
         
        ax_volume = fig.add_subplot(3, num, indexs[1][i], sharex=ax_k)
        draw_volumes(ax_volume, data)
         
        ax_macd = fig.add_subplot(3, num, indexs[2][i], sharex=ax_k)
        draw_macd(ax_macd, data)        

#     #weekly TA
#     w_data = ts.get_k_data(code_id, ktype="W", index=True, start='2015-6-30')    
#     
#     w_ax_k = fig.add_subplot(3, 2, 1)
#     w_ax_k.set_title("Week Technical Analyzation")
#     draw_candle_stick(w_ax_k, w_data)
#     
#     w_ax_volume = fig.add_subplot(3, 2, 3, sharex=w_ax_k)
#     draw_volumes(w_ax_volume, w_data)
#     
#     w_ax_macd = fig.add_subplot(3, 2, 5, sharex=w_ax_k)
#     draw_macd(w_ax_macd, w_data)
# 
#     d_data = ts.get_k_data(code_id, index=True, start='2017-05-01')    
# #     fig = plt.figure()
#     d_ax_k = fig.add_subplot(3, 2, 2)
#     d_ax_k.set_title("Day Technical Analyzation")
#     draw_candle_stick(d_ax_k, d_data)
#     
#     d_ax_volume = fig.add_subplot(3, 2, 4, sharex=d_ax_k)
#     draw_volumes(d_ax_volume, d_data)
#     
#     d_ax_macd = fig.add_subplot(3, 2, 6, sharex=d_ax_k)
#     draw_macd(d_ax_macd, d_data)

    plt.grid()
    plt.savefig(fname)    
#     plt.show()


# def get_start_date(ktype):
#     '''
#     ktype：string
#         数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D    
#     '''
#     if "M" in ktype:
#         return "2012-01-01"
#     elif "W" in ktype:
#         return "2016-10-30"    
#     elif "D" in ktype:
#         return "2017-05-01"
#     elif "60" in ktype:
#         return "2017-08-01"
#     elif "30" in ktype:
#         return "2017-09-01"
#     elif "15" in ktype:
#         return "2017-09-15"
#     elif "5" in ktype:
#         return "2017-10-15"            



def get_chart_title(ktype):
    '''
    ktype：string
        数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D    
    '''
    if "M" in ktype:
        return "Month TA"
    elif "W" in ktype:
        return "Week TA"    
    elif "D" in ktype:
        return "Day TA"
    elif "60" in ktype:
        return "60F TA"
    elif "30" in ktype:
        return "30F TA"
    elif "15" in ktype:
        return "15F TA"
    elif "5" in ktype:
        return "5F TA"
    else:
        return None  

if __name__ == '__main__':
#     code_id = "399300"
#     draw_stock_with_multi_periods(code_id, ["30", "15"], code_id + ".png")
                                   
#     print get_start_date("D")
#     num = 3
#     for i in xrange(num):
# #         print i, i*num + 1, i*num + 3, i*num + 5
    
#     aa = np.arange(1, 3*num+1).reshape(3, num)
#     print aa
#     for i in xrange(num):
#         print aa[0][i], aa[1][i], aa[2][i]

    print get_start_date("W")
