import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def report(symbol):
    url = api_ref.report_latest_url+symbol
    return utls.fetch(url)


def earningforecast(symbol):
    url = api_ref.report_earningforecast_url+symbol
    return utls.fetch(url)
