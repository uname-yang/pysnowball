from pysnowball import api_ref
from pysnowball import utls


def fund_detail(fund_code):
    return utls.fetch_danjuan_fund(api_ref.fund_detail % fund_code)


def fund_info(fund_code):
    return utls.fetch_danjuan_fund(api_ref.fund_info % fund_code)


def fund_growth(fund_code, day='ty'):
    '''
    Args:
        day: 'ty' (default) - this year,'1m','3m','6m','1y','2y','3y','5y','all'
    '''
    return utls.fetch_danjuan_fund(api_ref.fund_growth % (fund_code, day))


def fund_nav_history(fund_code, page=1, size=10):
    return utls.fetch_danjuan_fund(api_ref.fund_nav_history % (fund_code, page, size))


def fund_achievement(fund_code):
    return utls.fetch_danjuan_fund(api_ref.fund_achievement % fund_code)


def fund_asset(fund_code):
    return utls.fetch_danjuan_fund(api_ref.fund_asset % fund_code)


def fund_manager(fund_code, post_status=1):
    return utls.fetch_danjuan_fund(api_ref.fund_manager % (fund_code, post_status))


def fund_trade_date(fund_code):
    return utls.fetch_danjuan_fund(api_ref.fund_trade_date % fund_code)


def fund_derived(fund_code):
    return utls.fetch_danjuan_fund(api_ref.fund_derived % fund_code)

def fund_yield(fund_code):
    return utls.fetch_danjuan_fund(api_ref.fund_yield % fund_code)

def fund_search(keywords):
    return utls.fetch_danjuan_fund(api_ref.fund_search % keywords)

def fund_exist(fund_code):
    return utls.fetch_danjuan_fund(api_ref.fund_exist % (fund_code if fund_code.startswith('F') else 'F'+fund_code))

def funds_add(fund_codes):
    ''' Add fund(s) to watch list
    Args:
        fund_codes: list of fund codes, e.g. ['F019918','F161039']
    '''
    payload = "symbols="
    for code in fund_codes:
        if not code.startswith('F'):
            code = 'F' + code
        payload += code + ','
    payload = payload if not payload.endswith(',') else payload[:-1]
    return utls.post_danjuan_fund(api_ref.funds_add, payload)

def funds_remove(fund_codes):
    ''' Remove fund(s) from watch list
    Args:
        fund_codes: list of fund codes, e.g. ['F019918','F161039']
    '''
    payload = "symbols="
    for code in fund_codes:
        if not code.startswith('F'):
            code = 'F' + code
        payload += code + ','
    payload = payload if not payload.endswith(',') else payload[:-1]
    return utls.post_danjuan_fund(api_ref.funds_remove, payload)