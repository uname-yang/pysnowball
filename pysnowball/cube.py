from pysnowball import api_ref
from pysnowball import utls

def nav_daily(symbol):
    url = api_ref.nav_daily + symbol
    return utls.fetch(url)

def rebalancing_history(symbol, count=20, page=1):
    url = api_ref.rebalancing_history + symbol
    url = url + "&count=" + str(count)
    url = url + "&page=" + str(page)
    return utls.fetch(url)