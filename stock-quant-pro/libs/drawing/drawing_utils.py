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
    '''
    draw candle sticks
    '''
    
    #calculate ema values
    ema5 = ema(np.array(data['close']), 5)
    ema10 = ema(np.array(data['close']), 10)
    ema20 = ema(np.array(data['close']), 20)
    ema30 = ema(np.array(data['close']), 30)
    ema60 = ema(np.array(data['close']), 60)
    ema120 = ema(np.array(data['close']), 120)
    
    #make these tick labels invisible
    plt.setp(ax.get_xticklabels(), visible=False)
    
    #slice data here and it will display more clear
    ax.plot(ema5[-80:], label='MA5')
    ax.plot(ema10[-80:], label='MA10', color="#FFFF08")
    ax.plot(ema20[-80:], label='MA20', color="#FF80FF")
    ax.plot(ema30[-80:], label='MA30', color="#00E600")   
    ax.plot(ema60[-80:], label='MA60', color="#02E2F4")
    ax.plot(ema120[-80:], label='MA120', color="#000000")    
    ax.legend(loc='upper left')
    
    _data = data[-80:]
    mpf.candlestick2_ochl(ax, _data['open'], _data['close'], _data['high'], _data['low'],
                     width=0.5, colorup='r', colordown='green',
                     alpha=0.6)

def draw_volumes(ax, data):
    '''
    draw volumes
    '''
    
    #calculate the EMA
    ema5 = ema(np.array(data['volume']), 5)
    ema10 = ema(np.array(data['volume']), 10)
    
    #make these tick labels invisible
    plt.setp(ax.get_xticklabels(), visible=False)
    
    #slice data here and it will display more clear
    ax.plot(ema5[-80:], label='MA5')
    ax.plot(ema10[-80:], label='MA10', color="#FFFF08")
    
    _data = data[-80:]
    ax.bar(_data['date'], _data['volume'], width=0.3, color='red', label="Volume")
    
def draw_macd(ax, data):
    '''
    Draw MACD plot
    '''
    diff, dea, _macd = macd(data['close'].values)

    #slice data here and it will display more clear
    _data = data[-80:]
    
    #set X ticks and labels
    ax.set_xticks(range(0, len(_data['date']), 10))       
    ax.set_xticklabels(_data['date'][::10], rotation=45)
    
    ax.plot(_data['date'], diff[-80:], label='DIFF')
    ax.plot(_data['date'], dea[-80:], label='DEA')
    ax.legend(loc='upper left')
    
    ax.bar(_data['date'], _macd[-80:], width=0.3, color='red', label="MACD")

def draw_stock_with_multi_periods(code_id, periods, fname, index=False):
    '''
    Draw the pictures with candle sticks, vlumes and MACD
    '''
    if len(periods) == 0:
        log.error("periods parameter doesn't have any valid values")
        return False

    fig = plt.figure(figsize=(40,20))
    num = len(periods)
    
    #create index
    indexs = np.arange(1, 3*num+1).reshape(3, num)

    for i in xrange(num):
        ktype = periods[i]
        data = ts.get_k_data(code_id, ktype=ktype, index=index)    
        ax_k = fig.add_subplot(3, num, indexs[0][i])
        ax_k.set_title(get_chart_title(ktype))
        draw_candle_stick(ax_k, data)
         
        ax_volume = fig.add_subplot(3, num, indexs[1][i], sharex=ax_k)
        draw_volumes(ax_volume, data)
         
        ax_macd = fig.add_subplot(3, num, indexs[2][i], sharex=ax_k)
        draw_macd(ax_macd, data)        

    plt.grid()
    plt.savefig(fname)    
#     plt.show()

    return True

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
