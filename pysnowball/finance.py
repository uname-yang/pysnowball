import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls



def cash_flow(symbol, is_annals=0, count=10):

    url = api_ref.finance_cash_flow_url+symbol
    
    if is_annals == 1:
        url = url + '&type=Q4'
    
    url = url + '&count='+str(count)

    return utls.fetch(url)

# ?symbol=BABA&type=all&is_detail=true&count=5
# ?symbol=BABA&type=Q4&is_detail=false&count=5
def cash_flow_v2(symbol, count=10, region='cn', type='all', is_detail=True):
    url = api_ref.finance_cash_flow_detail_url.format(region,symbol,type,str(is_detail).lower(),str(count))

    return utls.fetch(url)


def indicator(symbol, is_annals=0, count=10):
    
    url = api_ref.finance_indicator_url+symbol
    
    if is_annals == 1:
        url = url + '&type=Q4'
    
    url = url + '&count='+str(count)

    return utls.fetch(url)


def indicator_v2(symbol, count=10, region='cn', type='all', is_detail=True):
    url = api_ref.finance_indicator_detail_url.format(region,symbol,type,str(is_detail).lower(),str(count))
    
    return utls.fetch(url)


def balance(symbol, is_annals=0, count=10):

    url = api_ref.finance_balance_url+symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url)


def balance_v2(symbol, count=10, region='cn', type='all', is_detail=True):
    url = api_ref.finance_balance_detail_url.format(region,symbol,type,str(is_detail).lower(),str(count))
    
    return utls.fetch(url)


def income(symbol, is_annals=0, count=10):
    
    url = api_ref.finance_income_url+symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url)

def income_v2(symbol, count=10, region='cn', type='all', is_detail=True):
    url = api_ref.finance_income_detail_url.format(region, symbol,type,str(is_detail).lower(),str(count))
    
    return utls.fetch(url)

def business(symbol, is_annals=0, count=10):

    url = api_ref.finance_business_url+symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url)
 
