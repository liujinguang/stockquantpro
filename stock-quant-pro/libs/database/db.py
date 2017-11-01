#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 31, 2017

@author: hadoop
'''

from datetime import datetime
from utils.time_utils import get_alert_interval
from utils.log import log

stock_pool = {
    "002352" : {"name":"顺风控股", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
    "002294" : {"name":"信立泰  ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
    "600887" : {"name":"伊利股份", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},	 
	"600298" : {"name":"安琪酵母", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},	
	"000895" : {"name":"双汇集团", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600104" : {"name":"上汽集团", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600572" : {"name":"康恩贝  ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600276" : {"name":"恒瑞医药", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600566" : {"name":"济川药业", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"000538" : {"name":"云南白药", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"601318" : {"name":"中国平安", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600056" : {"name":"中国医药", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"603288" : {"name":"海天味业", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002027" : {"name":"分众传媒", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"000581" : {"name":"威孚高科", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600741" : {"name":"华域汽车", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"000858" : {"name":"五粮液  ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600519" : {"name":"贵州茅台", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002422" : {"name":"科伦药业", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002081" : {"name":"金螳螂  ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002470" : {"name":"金正大  ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002517" : {"name":"恺英网络", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"300549" : {"name":"优德精密", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"603520" : {"name":"司立太  ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600176" : {"name":"中国巨石", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002008" : {"name":"大族激光", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002745" : {"name":"木林森  ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600585" : {"name":"海螺水泥", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002372" : {"name":"伟星新材", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600900" : {"name":"长江电力", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"601006" : {"name":"大秦铁路", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600518" : {"name":"康美药业", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002202" : {"name":"金凤科技", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002310" : {"name":"东方园林", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"000963" : {"name":"华东医药", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"601933" : {"name":"永辉超市", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002466" : {"name":"天齐锂业", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002475" : {"name":"立讯精密", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002241" : {"name":"歌尔股份", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600196" : {"name":"复星医药", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002572" : {"name":"索菲亚  ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600816" : {"name":"安信信托", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002415" : {"name":"海康威视", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"000333" : {"name":"美的集团", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002508" : {"name":"老板电器", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600660" : {"name":"福耀玻璃", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600201" : {"name":"生物股份", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"000002" : {"name":"万科股份", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002450" : {"name":"康得新  ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600009" : {"name":"上海机场", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600377" : {"name":"宁沪高速", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002597" : {"name":"金禾实业", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"601012" : {"name":"隆基股份", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"000725" : {"name":"京东方  ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600703" : {"name":"三安光电", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600699" : {"name":"均胜电子", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600036" : {"name":"招商银行", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"601888" : {"name":"中国国旅", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600019" : {"name":"宝钢股份", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600352" : {"name":"浙江龙盛", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600487" : {"name":"亨通光电", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"300498" : {"name":"温式股份", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"601607" : {"name":"上海医药", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"000651" : {"name":"格力电器", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"000100" : {"name":"TCL集团 ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"000063" : {"name":"中兴通信", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600570" : {"name":"恒生电子", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002074" : {"name":"国轩高科", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"603993" : {"name":"洛阳钼也", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600507" : {"name":"方大特钢", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"601211" : {"name":"国泰君安", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"601088" : {"name":"中国神华", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002594" : {"name":"比亚迪  ", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"002601" : {"name":"龙蟒百利", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600337" : {"name":"美克家居", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"300450" : {"name":"先导智能", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"000488" : {"name":"晨鸣纸业", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"600309" : {"name":"万华化学", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	"300274" : {"name":"阳光电源", "index":False, "In":False, "15F_alert_time":None, "30F_alert_time":None},
	
    }


def get_stock_pool():
    return stock_pool

def get_stock_list():
    return stock_pool.keys()

def is_index(code_id):
    return stock_pool[code_id]["index"]
    
def update_alert_time(code_id, ktype):
    '''
    update alert time
    '''
    log.info("update alert time for " + code_id + " " + ktype)
    if "15" in ktype:
        stock_pool[code_id]["15F_alert_time"] = datetime.now()
    else:
        stock_pool[code_id]["30F_alert_time"] = datetime.now()

def get_stock_name(code_id):
    '''
    '''
    return stock_pool[code_id]["name"]

def get_alert_time(code_id, ktype):
    '''
    '''
    if "15" in ktype:
        return stock_pool[code_id]["15F_alert_time"]
    else:
        return stock_pool[code_id]["30F_alert_time"]
    
def is_alert_needed(code_id, ktype):
    '''
    we need to check if the alert email is sent recently
    '''
    if "15" in ktype:
        last_alert_time = stock_pool[code_id]["15F_alert_time"]
    else:
        last_alert_time = stock_pool[code_id]["30F_alert_time"]   

    if last_alert_time is None:
        return True
    
    interval_time = datetime.now() - last_alert_time
    if interval_time.total_seconds() - get_alert_interval(ktype) > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    pass