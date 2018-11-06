import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def report(symbol, count=10):
    url = api_ref.report_latest_url+symbol
    # url = url + '&count='+str(count)
    return utls.fetch(url)


def earningforecast(symbol):
    url = api_ref.report_earningforecast_url+symbol
    return utls.fetch(url)
