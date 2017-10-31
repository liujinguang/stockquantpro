#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月30日

@author: bob
'''

from indictors.macd import macd

import matplotlib.pyplot as plt
import tushare as ts


if __name__ == '__main__':
    data = ts.get_k_data('399300', start='2017-01-01')
    
    diff, dea, macd = macd(data['close'].values)
# 
#     fig = plt.figure(figsize=[18, 5])
#       
#     ax = fig.add_subplot(1, 1, 1)
#     ax.set_xticks(range(0, len(data['date']), 10))
#        
#     ax.set_xticklabels(data['date'][::10], rotation=45)
#     
#     ax.plot(data['date'], diff, label='DIFF')
#     ax.plot(data['date'], dea, label='DEA')
#     ax.legend(loc='upper left')
#     
#     ax.bar(data['date'], macd, width=0.4, color='red', label="MACD")
     
    print macd[-1], diff[-1], dea[-1]
    print macd[-5], diff[-5], dea[-5]
    print diff[-1] > dea[-1]
#     
#     plt.grid()    
#     plt.show()    