from datetime import datetime
from datetime import timedelta
from pysnowball import api_ref
from pysnowball import utls


def index_basic_info(symbols):
    url = api_ref.index_basic_info.format(symbols)
    return utls.fetch_csindex(url)


def index_details_data(symbols):
    url = api_ref.index_details_data.format(symbols)
    return utls.fetch_csindex(url)


def index_weight_top10(symbols):
    url = api_ref.index_weight_top10.format(symbols)
    return utls.fetch_csindex(url)


def index_perf_7(symbols):
    today = datetime.now()
    firstday = today - timedelta(days=7)
    url = api_ref.index_perf.format(symbols, datetime.strftime(
        firstday, "%Y%m%d"), datetime.strftime(today, "%Y%m%d"))
    return utls.fetch_csindex(url)


def index_perf_30(symbols):
    today = datetime.now()
    firstday = today - timedelta(days=30)
    url = api_ref.index_perf.format(symbols, datetime.strftime(
        firstday, "%Y%m%d"), datetime.strftime(today, "%Y%m%d"))
    return utls.fetch_csindex(url)


def index_perf_90(symbols):
    today = datetime.now()
    firstday = today - timedelta(days=90)
    url = api_ref.index_perf.format(symbols, datetime.strftime(
        firstday, "%Y%m%d"), datetime.strftime(today, "%Y%m%d"))
    return utls.fetch_csindex(url)
