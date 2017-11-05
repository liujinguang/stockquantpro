#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月4日

@author: bob
'''

from datetime import datetime

import platform
import os


def get_charts_root_directory():
    if platform.system() == "Linux":
        rdir = '/home/hadoop/quant/' + datetime.now().strftime("%Y-%m-%d")
    else:
        rdir = 'd:\\quant\\' + datetime.now().strftime("%Y-%m-%d")
        
    if not os.path.exists(rdir):
        os.mkdir(rdir)    
        
    return rdir

if __name__ == '__main__':
    pass