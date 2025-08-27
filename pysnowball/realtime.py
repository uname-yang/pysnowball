import time
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def quotec(symbols):
    url = api_ref.realtime_quote+symbols
    return utls.fetch_without_token(url)


def quote_detail(symbol):
    return utls.fetch(api_ref.realtime_quote_detail+symbol)


def pankou(symbol):
    url = api_ref.realtime_pankou+symbol
    return utls.fetch(url)

def kline(symbol,begin=int(time.time()*1000),period='day',count=284):
    ''' Get kline data
    Args:
        symbol: stock symbol, e.g. 'SZ000001'
        begain: timestamp in milliseconds = int(time.time()*1000), default current time
        count: number of data points to fetch, default 284 (fetch all available data)
        period: '1m', '5m', '15m', '30m', '60m', 'day', 'week', 'month', 'quarter','year'
    '''
    return utls.fetch(api_ref.kline.format(symbol, begin, period, count))
