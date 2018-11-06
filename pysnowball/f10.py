import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def skholderchg(symbol):
    url = api_ref.f10_skholderchg+symbol
    return utls.fetch(url)


def skholder(symbol):
    url = api_ref.f10_skholder+symbol
    return utls.fetch(url)


def industry(symbol):
    url = api_ref.f10_industry+symbol
    return utls.fetch(url)


def holders(symbol):
    url = api_ref.f10_holders+symbol
    return utls.fetch(url)


def bonus(symbol,page=1,size=10):
    url = api_ref.f10_bonus+symbol
    url = url + '&page='+str(page)
    url = url + '&size='+str(size)
    return utls.fetch(url)


def org_holding_change(symbol):
    url = api_ref.f10_org_holding_change+symbol
    return utls.fetch(url)


def industry_compare(symbol):
    url = api_ref.f10_industry_compare+symbol
    return utls.fetch(url)


def business_analysis(symbol):
    url = api_ref.f10_business_analysis+symbol
    return utls.fetch(url)


def shareschg(symbol, count=5):
    url = api_ref.f10_shareschg+symbol
    url = url + '&count='+str(count)
    return utls.fetch(url)


def top_holders(symbol, circula=1):
    url = api_ref.f10_top_holders+symbol
    url = url + '&circula='+str(circula)
    return utls.fetch(url)


def main_indicator(symbol):
    url = api_ref.f10_indicator+symbol
    return utls.fetch(url)
