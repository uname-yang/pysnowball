from unittest import TestCase

from pysnowball import fund

test_fund_code = "008975"


class Test(TestCase):
    def test_fund_detail(self):
        fund_detail = fund.fund_detail(test_fund_code)
        print(fund_detail)

    def test_fund_info(self):
        fund_info = fund.fund_info(test_fund_code)
        print(fund_info)

    def test_fund_growth(self):
        fund_growth = fund.fund_growth(test_fund_code)
        print(fund_growth)

    def test_fund_nav_history(self):
        history = fund.fund_nav_history(test_fund_code)
        print(history)

    def test_fund_achievement(self):
        fund_achievement = fund.fund_achievement(test_fund_code)
        print(fund_achievement)

    def test_fund_asset(self):
        fund_asset = fund.fund_asset(test_fund_code)
        print(fund_asset)

    def test_fund_manager(self):
        fund_manager = fund.fund_manager(test_fund_code)
        print(fund_manager)

    def test_fund_trade_date(self):
        fund_trade_date = fund.fund_trade_date(test_fund_code)
        print(fund_trade_date)

    def test_fund_derived(self):
        fund_derived = fund.fund_derived(test_fund_code)
        print(fund_derived)
