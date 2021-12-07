from pysnowball import api_ref
from pysnowball import utls


def detail(symbol):
    return utls.fetch(api_ref.quote_detail % symbol)
