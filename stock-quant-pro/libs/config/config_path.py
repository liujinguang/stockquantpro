# encoding: UTF-8

from __future__ import print_function
import os


# _test_dir = os.path.dirname(os.path.abspath(__file__))
# DATA_CONFIG_PATH = os.path.abspath(os.path.join(_test_dir, 'data_config.json'))
# TRADE_CONFIG_PATH = os.path.abspath(os.path.join(_test_dir, 'trade_config.json'))
# 
# print("Current data config file path: {}".format(DATA_CONFIG_PATH))
# print("Current trade config file path: {}".format(TRADE_CONFIG_PATH))


def get_data_config_path():
    '''
    '''
    _test_dir = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.abspath(os.path.join(_test_dir, 'data_config.json'))

def get_trader_config_path():
    '''
    '''
    _test_dir = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.abspath(os.path.join(_test_dir, 'trade_config.json'))
