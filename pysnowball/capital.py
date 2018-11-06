import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def margin(symbol, page=1, size=180):
    url = api_ref.capital_margin_url+symbol
    url = url + '&page='+str(page)
    url = url + '&size='+str(size)
    return utls.fetch(url)


def blocktrans(symbol, page=1, size=30):
    url = api_ref.capital_blocktrans_url+symbol
    url = url + '&page='+str(page)
    url = url + '&size='+str(size)
    return utls.fetch(url)


def capital_assort(symbol):
    url = api_ref.capital_assort_url+symbol
    return utls.fetch(url)


def capital_flow(symbol):
    url = api_ref.capital_flow_url+symbol
    return utls.fetch(url)


def capital_history(symbol, count=20):
    url = api_ref.capital_history_url+symbol
    url = url + '&count='+str(count)
    return utls.fetch(url)
