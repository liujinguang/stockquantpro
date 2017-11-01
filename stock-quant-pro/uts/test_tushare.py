#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

import tushare as ts

if __name__ == '__main__':
#     data = ts.get_k_data("002352", ktype="60", index=False, start="2017-10-20")
#     print data[data.date >= "2017-10-20"]
#     print type(data)
#     print len(data)
#     ts.get_hist_data
#     dd = ts.get_today_all()
#     for d in dd.values:
#         print "\"" + d[0] + "\" : " + "\"" +  d[1] + "\","
    aa = ts.get_realtime_quotes("002352")
    print aa["ask"]

