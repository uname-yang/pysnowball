from pysnowball import api_ref
from pysnowball import utls

host = "xueqiu.com"

def suggest_stock(keyword):
    url = api_ref.suggest_stock + keyword
    return utls.fetch(url, host)