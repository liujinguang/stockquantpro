#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Nov 3, 2017

@author: hadoop
'''

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')
    subparser1 = subparsers.add_parser('1')
    subparser1.add_argument('-x')
    subparser2 = subparsers.add_parser('2')
    subparser2.add_argument('y')
    print parser.parse_args()
