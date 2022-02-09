# -*- coding:utf-8 -*-
from __future__ import print_function



import json
import os
import logging
from bs4 import BeautifulSoup

from pysnowball import utls
from pysnowball import api_ref

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


def northbound_shareholding_sh(txt_date=None):
    """
    date: '%Y/%m/%d'
    """
    return _get_shareholding('sh', txt_date)


def northbound_shareholding_sz(txt_date=None):
    """
    date: '%Y/%m/%d'
    """
    return _get_shareholding('sz', txt_date)


def _get_shareholding(exchange, txt_date):
    try:
        html = utls.fetch_hkc(api_ref.hkex_connect + exchange.lower(), txt_date)
        bsObj = BeautifulSoup(html, "html.parser")
        data = []
        for tr in bsObj.find("table", {"id": "mutualmarket-result"}).find("tbody").findAll("tr"):
            code = tr.find("td", {"class": "col-stock-code"}
                           ).find("div", {"class": "mobile-list-body"}).get_text()
            name = tr.find("td", {"class": "col-stock-name"}
                           ).find("div", {"class": "mobile-list-body"}).get_text()
            shareholding = tr.find("td", {"class": "col-shareholding"}
                                   ).find("div", {"class": "mobile-list-body"}).get_text()
            shareholding_percent = tr.find("td", {"class": "col-shareholding-percent"}
                                           ).find("div", {"class": "mobile-list-body"}).get_text()
            shareholding = int(shareholding.replace(',',''))
            data.append({
                'code':code,
                'name':name,
                'shareholding':shareholding,
                'shareholding_percent':shareholding_percent
            })
        return data
    except Exception as e:
        logger.error(e)


# | from | 70 | 71 | 72 | 73 | 77 | 78 | 90 | 91 | 93 | 95 | 30 |
# | to   |000 |001 |002 |003 |300 |301 |600 |601 |603 |605 |688 |

def tran_code(code):
    code_str = str(code)
    d2 = code_str[0:2]
    d3 = code_str[2:5]

    if d2 == "70":
        return 'SZ000'+d3
    elif d2 == "71":
        return 'SZ001'+d3
    elif d2 == "72":
        return 'SZ002'+d3
    elif d2 == "73":
        return 'SZ003'+d3
    elif d2 == "77":
        return 'SZ300'+d3
    elif d2 == "78":
        return 'SZ301'+d3
    elif d2 == "90":
        return 'SH600'+d3
    elif d2 == "91":
        return 'SH601'+d3
    elif d2 == "92":
        return 'SH602'+d3
    elif d2 == "93":
        return 'SH603'+d3
    elif d2 == "94":
        return 'SH604'+d3
    elif d2 == "95":
        return 'SH605'+d3
    elif d2 == "30":
        return 'SH688'+d3
    else:
        logger.error('tran_code error:'+code_str)
        raise('tran_code error:'+code_str)

