from pysnowball import api_ref
from pysnowball import utls

host = "xueqiu.com"

def watch_list():
    url = api_ref.watch_list
    return utls.fetch(url)

def watch_stock(id):
    url = api_ref.watch_stock + str(id)
    return utls.fetch(url)

def user_timeline(user_id, page=1, count=20, type=None, source=None):
    url = api_ref.user_timeline_url.format(user_id, page, count)
    if type is not None:
        url += "&type=" + str(type)
    if source is not None:
        url += "&source=" + source
    return utls.fetch(url, host)

def home_timeline(source="user", page=1, count=20):
    url = api_ref.home_timeline_url.format(source, page, count)
    return utls.fetch(url, host)

def user_favorites(user_id, size=20):
    url = api_ref.user_favorites_url.format(user_id, size)
    return utls.fetch(url, host)
