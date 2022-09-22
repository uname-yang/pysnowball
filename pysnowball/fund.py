from pysnowball import api_ref
from pysnowball import utls


def fund_detail(fund_code):
    return utls.fetch_danjuan_fund(api_ref.fund_detail % fund_code)


def fund_info(fund_code):
    return utls.fetch_danjuan_fund(api_ref.fund_info % fund_code)


def fund_growth(fund_code, day='ty'):
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
