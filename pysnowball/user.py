from pysnowball import api_ref
from pysnowball import utls

def watch_list():
    url = api_ref.watch_list
    return utls.fetch(url)

def watch_stock(id):
    url = api_ref.watch_stock + str(id)
    return utls.fetch(url)