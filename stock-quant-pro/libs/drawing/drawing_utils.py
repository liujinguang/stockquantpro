# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月30日

@author: bob
'''

from indictors.ema import ema
from indictors.macd import macd
from utils.log import log
from datetime import datetime

import os
import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import numpy as np
import platform

def draw_candle_stick(ax, data, pnum=120):
    '''
    draw candle sticks
    '''
    
    # calculate ema values
    ema5 = ema(np.array(data['close']), 5)
    ema10 = ema(np.array(data['close']), 10)
    ema20 = ema(np.array(data['close']), 20)
    ema30 = ema(np.array(data['close']), 30)
    ema60 = ema(np.array(data['close']), 60)
    ema120 = ema(np.array(data['close']), 120)
    
    # make these tick labels invisible
    plt.setp(ax.get_xticklabels(), visible=False)
    
    # slice data here and it will display more clear
    _ema5 = ema5[-pnum:]
    _ema10 = ema10[-pnum:]
    _ema20 = ema20[-pnum:]
    _ema30 = ema30[-pnum:]
    _ema60 = ema60[-pnum:]
    _ema120 = ema120[-pnum:]
    
    ax.plot(_ema5, label='MA5=%f' % _ema5[-1])
    ax.plot(_ema10, label='MA10=%f' % _ema10[-1], color="#FFFF08")
    ax.plot(_ema20, label='MA20=%f' % _ema20[-1], color="#FF80FF")
    if _ema30.size > 0:
        ax.plot(_ema30, label='MA30=%f' % _ema30[-1], color="#00E600")
    if _ema60.size > 0:
        ax.plot(_ema60, label='MA60=%f' % _ema60[-1], color="#02E2F4")
    if _ema120.size > 0:
        ax.plot(_ema120, label='MA120=%f' % _ema120[-1], color="#000000")
    ax.legend(loc='upper left')
    
    _data = data[-pnum:]
    mpf.candlestick2_ochl(ax, _data['open'], _data['close'], _data['high'], _data['low'],
                     width=0.5, colorup='r', colordown='green',
                     alpha=0.6)

def draw_volumes(ax, data, pnum=120):
    '''
    draw volumes
    '''
    
    # calculate the EMA
    ema5 = ema(np.array(data['volume']), 5)
    ema10 = ema(np.array(data['volume']), 10)
    
    # make these tick labels invisible
    plt.setp(ax.get_xticklabels(), visible=False)
    
    # slice data here and it will display more clear
    ax.plot(ema5[-pnum:], label='MA5')
    ax.plot(ema10[-pnum:], label='MA10', color="#FFFF08")
    
    _data = data[-pnum:]
    ax.bar(_data['date'], _data['volume'], width=0.3, color='red', label="Volume")
    
def draw_macd(ax, data, pnum=120):
    '''
    Draw MACD plot
    '''
    diff, dea, _macd = macd(data['close'].values)

    # slice data here and it will display more clear
    _data = data[-pnum:]
    
    # set X ticks and labels
    ax.set_xticks(range(0, len(_data['date']), 10))       
    ax.set_xticklabels(_data['date'][::10], rotation=45)
    
    ax.plot(_data['date'], diff[-pnum:], LineWidth=2, label='DIFF')
    ax.plot(_data['date'], dea[-pnum:], LineWidth=2, label='DEA')
    ax.legend(loc='upper left')
    
    _macd_tmp = _macd[-pnum:]
    
    if _macd_tmp.size == pnum:
        _macd_above_zero = np.zeros(pnum)
        _macd_below_zero = np.zeros(pnum)        
        for i in xrange(pnum):
            if _macd_tmp[i] > 0:
                _macd_above_zero[i] = _macd_tmp[i]
            else:
                _macd_below_zero[i] = _macd_tmp[i]
    else:
        _macd_above_zero = np.zeros(_macd_tmp.size)
        _macd_below_zero = np.zeros(_macd_tmp.size)        
        for i in xrange(_macd_tmp.size):
            if _macd_tmp[i] > 0:
                _macd_above_zero[i] = _macd_tmp[i]
            else:
                _macd_below_zero[i] = _macd_tmp[i]        
    
#     ax.bar(_data['date'], _macd[-pnum:], width=0.3, color='red', label="MACD")
    ax.bar(_data['date'], _macd_above_zero, width=0.3, color='red', label="MACD")
    ax.bar(_data['date'], _macd_below_zero, width=0.3, color='green', label="MACD")

def draw_stock_with_multi_periods(code_id, periods, fname, index=False):
    '''
    Draw the pictures with candle sticks, vlumes and MACD
    '''
    if len(periods) == 0:
        log.error("periods parameter doesn't have any valid values")
        return False

    fig = plt.figure(figsize=(40, 20))
    num = len(periods)
    
    # create index
    indexs = np.arange(1, 3 * num + 1).reshape(3, num)

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
    plt.close(fig)  
    
#     plt.show()

    return True

def draw_stock_with_multi_periods2(code_id, periods, fname, index=False):
    '''
    Draw the pictures with candle sticks, vlumes and MACD
    '''
    if len(periods) == 0:
        log.error("periods parameter doesn't have any valid values")
        return False

    fig = plt.figure(figsize=(40, 80))
    num = len(periods)
    
#     total_plots = num * 3
    # create index
    indexs = np.arange(1, 19).reshape(9, 2)
    print indexs[0][0]

    for i in xrange(num):
        ktype = periods[i]
        data = ts.get_k_data(code_id, ktype=ktype, index=index)    
        ax_k = fig.add_subplot(9, 2, indexs[i / 2 * 3][i % 2])
        ax_k.set_title(get_chart_title(ktype))
        draw_candle_stick(ax_k, data)
         
        ax_volume = fig.add_subplot(9, 2, indexs[i / 2 * 3 + 1][i % 2], sharex=ax_k)
        draw_volumes(ax_volume, data)
         
        ax_macd = fig.add_subplot(9, 2, indexs[i / 2 * 3 + 2][i % 2], sharex=ax_k)
        draw_macd(ax_macd, data)        

    plt.grid()
    plt.savefig(fname)  
    plt.close(fig)  
    
#     plt.show()

    return True

def draw_stock_with_candlestick_macd(code_id, periods, fname, index=False):
    '''
    Draw the pictures with candle sticks, volumes and MACD
    '''
    num = len(periods)
    if (num == 0) or (num % 2 != 0):
        log.error("periods parameter doesn't have any valid values")
        log.error("It accepts even numbers for periods parameter")
        return False

    fig = plt.figure(figsize=(80, 40))
    
    # create index
    indexs = np.arange(1, 2 * num + 1).reshape(num, 2)
    
    if num == 2:
        pnum = 160
    else:
        pnum = 120

    for i in xrange(num):
        ktype = periods[i]
        data = ts.get_k_data(code_id, ktype=ktype, index=index)    
        ax_k = fig.add_subplot(num, 2, indexs[i / 2 * 2][i % 2])
        ax_k.set_title(get_chart_title(ktype))
        draw_candle_stick(ax_k, data, pnum)
         
#         ax_volume = fig.add_subplot(6, 2, indexs[i/2*3 + 1][i%2], sharex=ax_k)
#         draw_volumes(ax_volume, data)
         
        ax_macd = fig.add_subplot(num, 2, indexs[i / 2 * 2 + 1][i % 2], sharex=ax_k)
        draw_macd(ax_macd, data, pnum)        

    print fname
    plt.grid()
    plt.savefig(fname)  
    plt.close(fig)  
    
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

def get_charts_root_dir(append=None):
    '''
    Get where charts should be stored
    '''
    if platform.system() == "Linux":
        rdir = '/home/hadoop/quant/' + datetime.now().strftime("%Y-%m-%d")
    else:
        rdir = 'd:\\quant\\' + datetime.now().strftime("%Y-%m-%d")
        
    if append is not None:
        rdir = rdir + append + os.sep
        
    if not os.path.exists(rdir):
        os.mkdir(rdir)  
        
    return rdir  

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
    pass
