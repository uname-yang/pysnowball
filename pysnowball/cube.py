from pysnowball import api_ref
from pysnowball import utls

def nav_daily(symbol):
    url = api_ref.nav_daily + symbol
    return utls.fetch(url)