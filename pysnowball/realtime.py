import json
import os
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
