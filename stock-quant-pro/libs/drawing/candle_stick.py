#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月30日

@author: bob
'''
from indictors.ema import ema

import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import numpy as np

def draw_candle_stick(ax, data, ktype, start=None):
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
    
    ax.set_xticks(range(0, len(data['date']), 10))
     
    ax.set_xticklabels(data['date'][::10], rotation=45)
    
    ax.plot(ema5, label='MA5')
    ax.plot(ema10, label='MA10', color="#FFFF08")
    ax.plot(ema20, label='MA20', color="#FF80FF")
    ax.plot(ema30, label='MA30', color="#00E600")   
    ax.plot(ema60, label='MA60', color="#02E2F4")
    ax.plot(ema120, label='MA120', color="#000000")    
    ax.legend(loc='upper left')
     
    mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'],
                     width=0.5, colorup='r', colordown='green',
                     alpha=0.6)
#     plt.grid()    
#     plt.show()


def draw_all_candle_stick(code_id):
    fig = plt.figure()
    ax = fig.add_subplot(3, 2, 1)
    


if __name__ == '__main__':
    pass