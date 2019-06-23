#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
import logging
from bs4 import BeautifulSoup
#from my_app.models import Fund

def get_fund_data(fund_num):
    """Get the data of fund.

    :param fund_num: a list contains the codes of fund
    :return: a dictionary
    """

    result = {}
    try:
        result_open = urlopen('http://www.dayfund.cn/fundvalue/{0}.html?sdate=2007-06-20&edate=2008-06-20'.format(fund_num)).read()  #.decode("utf-8")
    except Exception, e:
        logging.error(e)
    else:
        result_bs = BeautifulSoup(result_open)
        for i in result_bs.find_all('tr', class_="row1"):
            tmp_res = {}
            tr = i.get_text().split('\n')
            if tr[1][0] == '2':
                #print tr[1], tr[4], tr[5], tr[-2]
                tmp_res['date'] = tr[1]
                tmp_res['nav'] = tr[4]
                tmp_res['cav'] = tr[5]
                tmp_res['rate'] = tr[-2]
                result[tr[1]] = tmp_res
            # Fund.objects.check(date=tr[1], nav=tr[4], cav=tr[5], rate=tr[-2])
            # break
    return result


fund_list = ['050002']
for i in fund_list:
    print get_fund_data(i)

