# pysnowball

> 雪球APP Python API (需要自取token)

## 快速指引

安装

```bash
pip install pysnowball
```

示例

```python
>>> import pysnowball as ball
>>> ball.set_token('xq_a_token=651af***************031c96a315c;')
'xq_a_token=651af***************031c96a315c;'
>>> ball.cash_flow('SH600000')
```

调用API前需要手动获取雪球网站的token,使用set_token设置token后才能访问雪球的API。

传送门 === [如何获取雪球token](https://blog.crackcreed.com/diy-xue-qiu-app-shu-ju-api/)

## 联系作者

> 欢迎加入Users微信群，方便讨论使用方面的问题，新需求，以及量化交易相关的内容。 共同进步！

![img](https://blog.crackcreed.com/content/images/2021/02/wechat_me-1.jpg)

![wx](https://github.com/uname-yang/pysnowball/blob/master/wx.png?raw=true)

## APIs

### 实时行情

获取某支股票的行情数据

```python
import pysnowball as ball
ball.quotec('SZ002027')
```

结果显示：

```json
{
    "data": [
        {
            "symbol": "SZ002027",
            "current": 1.341,
            "percent": -0.89,
            "chg": -0.012,
            "timestamp": 1541486940000,
            "volume": 2695183,
            "amount": 3605340,
            "market_capital": 9835440347.54,
            "float_market_capital": null,
            "turnover_rate": null,
            "amplitude": 1.4,
            "open": 1.351,
            "last_close": 1.353,
            "high": 1.351,
            "low": 1.332,
            "avg_price": 1.338,
            "trade_volume": 22100,
            "side": 1,
            "is_trade": true,
            "level": 1,
            "trade_session": null,
            "trade_type": null,
            "current_year_percent": -35.84
        }
    ],
    "error_code": 0,
    "error_description": null
}
```

获取某支股票的行情数据-详细

```python
import pysnowball as ball
ball.quote_detail("SH600104")
```

结果显示：

```json
{
    "data": {
        "market": {
            "status_id": 7,
            "region": "CN",
            "status": "已收盘",
            "time_zone": "Asia/Shanghai",
            "time_zone_desc": null,
            "delay_tag": 0
        },
        "quote": {
            "current_ext": null,
            "symbol": "SH600104",
            "volume_ext": null,
            "high52w": 26.4319,
            "delayed": 0,
            "type": 11,
            "tick_size": 0.01,
            "float_shares": 11683461365,
            "limit_down": 18.23,
            "no_profit": null,
            "high": 20.96,
            "float_market_capital": 2.43717004074E11,
            "timestamp_ext": null,
            "lot_size": 100,
            "lock_set": null,
            "weighted_voting_rights": null,
            "chg": 0.61,
            "eps": 2.07,
            "last_close": 20.25,
            "profit_four": 2.413305412205E10,
            "volume": 65949501,
            "volume_ratio": 1.73,
            "profit_forecast": 2.7133061018E10,
            "turnover_rate": 0.56,
            "low52w": 18.03,
            "name": "上汽集团",
            "exchange": "SH",
            "pe_forecast": 8.982,
            "total_shares": 11683461365,
            "status": 1,
            "is_vie_desc": null,
            "security_status": null,
            "code": "600104",
            "goodwill_in_net_assets": 0.5219986746082667,
            "avg_price": 20.698,
            "percent": 3.01,
            "weighted_voting_rights_desc": null,
            "amplitude": 3.51,
            "current": 20.86,
            "is_vie": null,
            "current_year_percent": -11.78,
            "issue_date": 880387200000,
            "sub_type": "ASH",
            "low": 20.25,
            "is_registration_desc": null,
            "no_profit_desc": null,
            "market_capital": 2.43717004074E11,
            "dividend": 0.62,
            "dividend_yield": 2.972,
            "currency": "CNY",
            "navps": 23.18,
            "profit": 2.043103747976E10,
            "timestamp": 1638860400000,
            "pe_lyr": 11.929,
            "amount": 1.365040096E9,
            "pledge_ratio": null,
            "traded_amount_ext": null,
            "is_registration": null,
            "pb": 0.9,
            "limit_up": 22.28,
            "pe_ttm": 10.099,
            "time": 1638860400000,
            "open": 20.33
        },
        "others": {
            "pankou_ratio": -29.27,
            "cyb_switch": true
        },
        "tags": [
            {
                "description": "沪股通",
                "value": 1
            },
            {
                "description": "融",
                "value": 6
            },
            {
                "description": "空",
                "value": 7
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 实时分笔

获取实时分笔数据，可以实时取得股票当前报价和成交信息

```python
import pysnowball as ball
ball.pankou('SZ002027')
```

结果显示：

```json
{
    "symbol": "SZ002027",
    "time": "Nov 6, 2018 2:59:15 PM",
    "timestamp": 1541487555000,
    "bp1": 6.56,
    "bc1": 502,
    "bp2": 0,
    "bc2": 0,
    "bp3": 0,
    "bc3": 0,
    "bp4": 0,
    "bc4": 0,
    "bp5": 0,
    "bc5": 0,
    "bp6": 0,
    "bc6": 0,
    "bp7": 0,
    "bc7": 0,
    "bp8": 0,
    "bc8": 0,
    "bp9": 0,
    "bc9": 0,
    "bp10": 0,
    "bc10": 0,
    "current": 6.55,
    "sp1": 6.56,
    "sc1": 502,
    "sp2": 0,
    "sc2": 2796,
    "sp3": 0,
    "sc3": 0,
    "sp4": 0,
    "sc4": 0,
    "sp5": 0,
    "sc5": 0,
    "sp6": 0,
    "sc6": 0,
    "sp7": 0,
    "sc7": 0,
    "sp8": 0,
    "sc8": 0,
    "sp9": 0,
    "sc9": 0,
    "sp10": 0,
    "sc10": 0,
    "buypct": 13.21,
    "sellpct": 86.79,
    "diff": -2796,
    "ratio": -73.58
}
```

### K线

获取实时分笔数据，可以实时取得股票当前报价和成交信息

```python
import pysnowball as ball
ball.kline('SZ002027')
ball.kline('SZ002027', 300)
```

[结果显示](APIs/realtime_kline.md)

### 业绩预告

按年度获取业绩预告数据

```python
import pysnowball as ball
ball.earningforecast('SZ002027')
```

结果显示：

```json
{
    "list": [
        {
            "eps": 4.78,
            "roe": null,
            "pb": null,
            "pe": 8.4,
            "forecast_year": "2018"
        },
        {
            "eps": 5.49,
            "roe": null,
            "pb": null,
            "pe": 7.32,
            "forecast_year": "2019"
        },
        {
            "eps": 6.12,
            "roe": null,
            "pb": null,
            "pe": 6.56,
            "forecast_year": "2020"
        }
    ]
}
```

### 机构评级

获取机构评级数据

```python
import pysnowball as ball
ball.report('SZ002027')
```

结果显示：

```json
{
    "list": [
        {
            "title": "2018年三季报点评：业绩确定性最强 新冷年预收款下降",
            "rpt_comp": "申万宏源",
            "rating_desc": "买入",
            "target_price_min": null,
            "target_price_max": null,
            "pub_date": 1541088000000,
            "status_id": 116200430,
            "retweet_count": 0,
            "reply_count": 4,
            "like_count": 4,
            "liked": false
        },
        {
            "title": "2018年三季报点评：业绩表现优异 现金流增长亮眼(",
            "rpt_comp": "海通证券",
            "rating_desc": "增持",
            "target_price_min": 50.3,
            "target_price_max": 60.4,
            "pub_date": 1541088000000,
            "status_id": 116196608,
            "retweet_count": 0,
            "reply_count": 0,
            "like_count": 0,
            "liked": false
        }...
    ]
}
```

### 资金流向趋势

获取当日资金流如流出数据，每分钟数据

```python
import pysnowball as ball
ball.capital_flow('SZ002027')
```

结果显示：

```json
{
    "data": {
        "symbol": "SZ002027",
        "items": [
            {
                "timestamp": 1541467800000,
                "amount": -12323447,
                "type": null
            },
            {
                "timestamp": 1541467860000,
                "amount": -12940471,
                "type": null
            },
            {
                "timestamp": 1541467920000,
                "amount": -18710425,
                "type": null
            },
            ...
    ]
}
```

### 资金流向历史

获取历史资金流如流出数据，每日数据

```python
import pysnowball as ball
ball.capital_history('SZ002027')
```

结果显示：

```json
{
    "data": {
        "sum3": -152759438,
        "sum5": -332530425,
        "sum10": -362575240.15999997,
        "sum20": -162580140.64,
        "items": [
            {
                "amount": 1232691,
                "timestamp": 1539100800000
            },
            {
                "amount": -65392886,
                "timestamp": 1539187200000
            },
            ...
            {
                "amount": -4122992,
                "timestamp": 1541433600000
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 资金成交分布

获取资金成交分布数据

```python
import pysnowball as ball
ball.capital_assort('SZ002027')
```

结果显示：

```json
{
    "data": {
        "sell_large": 21922533,
        "sell_medium": 353650388,
        "sell_small": 225596826,
        "sell_total": 601169747,
        "buy_large": 14298615,
        "buy_medium": 317379444,
        "buy_small": 265530036,
        "buy_total": 597208095,
        "timestamp": 1541433600000,
        "created_at": null,
        "updated_at": null
    },
    "error_code": 0,
    "error_description": ""
}
```

### 大宗交易

大宗交易数据

```python
import pysnowball as ball
ball.blocktrans('SZ002027')
```

结果显示：

```json
{
    "data": {
        "items": [
            {
                "vol": 780200,
                "sell_branch_org_name": "机构专用",
                "premium_rat": 0,
                "trans_amt": 30193700,
                "td_date": 1541001600000,
                "buy_branch_org_name": "机构专用",
                "trans_price": 38.7
            },
            {
                "vol": 774200,
                "sell_branch_org_name": "机构专用",
                "premium_rat": 0,
                "trans_amt": 29961500,
                "td_date": 1541001600000,
                "buy_branch_org_name": "机构专用",
                "trans_price": 38.7
            },
            ...
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 融资融券

融资融券数据

```python
import pysnowball as ball
ball.margin('SZ002027')
```

结果显示：

```json
{
    "data": {
        "items": [
            {
                "margin_trading_amt_balance": 960745756,
                "short_selling_amt_balance": 2888439,
                "margin_trading_balance": 957857317,
                "td_date": 1541347200000
            },
            {
                "margin_trading_amt_balance": 948660728,
                "short_selling_amt_balance": 2767982,
                "margin_trading_balance": 945892746,
                "td_date": 1541088000000
            },
            ...
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 业绩指标

按年度、季度获取业绩报表数据。

```python
import pysnowball as ball
ball.indicator('SZ002027')
# or
ball.indicator(symbol='SZ002027',is_annals=1,count=10)
```

输入参数：

* symbol -> 股票代码
* is_annals -> 只获取年报,默认为1
* count -> 返回数据数量,默认5条

结果显示：

```json
{
    "data": {
        "quote_name": "分众传媒",
        "currency_name": "人民币",
        "org_type": 1,
        "last_report_name": "2018三季报",
        "currency": "CNY",
        "list": [
            {
                "report_date": 1538236800000,
                "report_name": "2018三季报",
                "avg_roe": [
                    40.2459,
                    -0.16318251756975927
                ],
                "np_per_share": [
                    0.9217,
                    0.3588382721509656
                ],
                "operate_cash_flow_ps": [
                    0.1063,
                    -0.45543032786885246
                ],
                "basic_eps": [
                    0.3277,
                    0.024062499999999952
                ],
                "capital_reserve": [
                    0.0127,
                    -0.15333333333333335
                ],
                "undistri_profit_ps": [
                    0.9042,
                    0.4481101857783473
                ],
                "net_interest_of_total_assets": [
                    28.1351,
                    -0.10744276201624894
                ],
                "gross_selling_rate": [
                    69.2402,
                    -0.042102277836574074
                ]
            },
            {
                "report_date": 1530288000000,
                "report_name": "2018中报",
                "avg_roe": [
                    29.2624,
                    -0.1387915228248617
                ],
                "np_per_share": [
                    0.85,
                    0.07336784947594384
                ],
                "operate_cash_flow_ps": [
                    0.085,
                    -0.5940783190066857
                ],
                "basic_eps": [
                    0.23,
                    -0.20689655172413784
                ],
                "capital_reserve": [
                    0.0127,
                    -0.3923444976076555
                ],
                "undistri_profit_ps": [
                    0.8046,
                    0.12405699916177702
                ],
                "net_interest_of_total_assets": [
                    20.1998,
                    0.06631263329039885
                ],
                "gross_selling_rate": [
                    71.8153,
                    0.014222928982801345
                ]
            },
            ...
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 利润表

```python
import pysnowball as ball
ball.income('SZ300251')
# or
ball.income(symbol='SZ300251',is_annals=1,count=10)
```

输入参数：

* symbol -> 股票代码
* is_annals -> 只获取年报,默认为1
* count -> 返回数据数量,默认5条

结果显示：

```json
{
    "data": {
        "quote_name": "光线传媒",
        "currency_name": "人民币",
        "org_type": 1,
        "last_report_name": "2018三季报",
        "currency": "CNY",
        "list": [
            {
                "report_date": 1514649600000,
                "report_name": "2017年报",
                "net_profit": [
                    815156857.46,
                    0.10020849906436384
                ],
                "net_profit_atsopc": [
                    815156857.46,
                    0.10020849906436384
                ],
                "total_revenue": [
                    1843452761.05,
                    0.06477235336668148
                ],
                "op": [
                    672007490.01,
                    -0.1544941646451226
                ]
            },
            {
                "report_date": 1483113600000,
                "report_name": "2016年报",
                "net_profit": [
                    740911252.87,
                    0.8426691031822198
                ],
                "net_profit_atsopc": [
                    740911252.87,
                    0.8426691031822198
                ],
                "total_revenue": [
                    1731311632.22,
                    0.13655725191234208
                ],
                "op": [
                    794799351.95,
                    0.8342603099386635
                ]
            },
            ...
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 资产负债表

```python
import pysnowball as ball
ball.balance('SZ300251')
# or
ball.balance(symbol='SZ300251',is_annals=1,count=10)
```

输入参数：

* symbol -> 股票代码
* is_annals -> 只获取年报,默认为1
* count -> 返回数据数量,默认5条

结果显示：

```json
{
    "data": {
        "quote_name": "光线传媒",
        "currency_name": "人民币",
        "org_type": 1,
        "last_report_name": "2018三季报",
        "currency": "CNY",
        "list": [
            {
                "report_date": 1514649600000,
                "report_name": "2017年报",
                "total_assets": [
                    11884462717.67,
                    0.2989175670473065
                ],
                "total_liab": [
                    3429697781.5,
                    0.6877450604731051
                ],
                "asset_liab_ratio": [
                    0.288586691967208,
                    0.2993473206384294
                ]
            },
            {
                "report_date": 1483113600000,
                "report_name": "2016年报",
                "total_assets": [
                    9149512655.13,
                    0.11726415171002368
                ],
                "total_liab": [
                    2032118393.84,
                    0.6680466814500612
                ],
                "asset_liab_ratio": [
                    0.2221012714486624,
                    0.49297431488967003
                ]
            },
            ...
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 现金流量表

```python
import pysnowball as ball
ball.cash_flow('SZ300251')
# or
ball.cash_flow(symbol='SZ300251',is_annals=1,count=10)
```

输入参数：

* symbol -> 股票代码
* is_annals -> 只获取年报,默认为1
* count -> 返回数据数量,默认5条

结果显示：

```json
{
    "data": {
        "quote_name": "光线传媒",
        "currency_name": "人民币",
        "org_type": 1,
        "last_report_name": "2018三季报",
        "currency": "CNY",
        "list": [
            {
                "report_date": 1538236800000,
                "report_name": "2018三季报",
                "ncf_from_oa": [
                    -299512204.39,
                    -15.69337270939856
                ],
                "ncf_from_ia": [
                    701876463.13,
                    2.493053545204141
                ],
                "ncf_from_fa": [
                    -1605703920.9,
                    -10.364167402276724
                ]
            },
            {
                "report_date": 1530288000000,
                "report_name": "2018中报",
                "ncf_from_oa": [
                    -181196373.81,
                    -1.7290892286108568
                ],
                "ncf_from_ia": [
                    2347407590.16,
                    3.905172712067323
                ],
                "ncf_from_fa": [
                    -586721686.4,
                    -4.271754192732585
                ]
            },
            ...
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### 主营业务构成

```python
import pysnowball as ball
ball.business('SZ300251')
# or
ball.business(symbol='SZ300251',count=10)
```

输入参数：

* symbol -> 股票代码
* count -> 返回数据数量,默认5条

结果显示：

```json
{
    "data": {
        "quote_name": "光线传媒",
        "currency": "CNY",
        "list": [
            {
                "report_date": 1530288000000,
                "report_name": "2018中报",
                "class_list": [
                    {
                        "class_standard": 2,
                        "business_list": [
                            {
                                "project_announced_name": "电影及衍生品",
                                "prime_operating_income": 472496159.52,
                                "income_ratio": 0.6554,
                                "gross_profit_rate": 0.4880141511292849
                            },
                            {
                                "project_announced_name": "电视剧",
                                "prime_operating_income": 235946734.18,
                                "income_ratio": 0.3273,
                                "gross_profit_rate": 0.41673913085394504
                            },
                            {
                                "project_announced_name": "游戏及其他",
                                "prime_operating_income": 12491524.81,
                                "income_ratio": 0.0173,
                                "gross_profit_rate": 0.34024031450488706
                            }
                        ]
                    }
                ]
            },
            {
                "report_date": 1514649600000,
                "report_name": "2017年报",
                "class_list": [
                    {
                        "class_standard": 1,
                        "business_list": [
                            {
                                "project_announced_name": "传媒",
                                "prime_operating_income": 1843452761.05,
                                "income_ratio": 1,
                                "gross_profit_rate": 0.4127651986897655
                            }
                        ]
                    },
                    {
                        "class_standard": 2,
                        "business_list": [
                            {
                                "project_announced_name": "电影及衍生品",
                                "prime_operating_income": 1238167750.17,
                                "income_ratio": 0.6717,
                                "gross_profit_rate": 0.44010894038807064
                            },
                            {
                                "project_announced_name": "视频直播",
                                "prime_operating_income": 491462820.98,
                                "income_ratio": 0.2666,
                                "gross_profit_rate": 0.33240443566869143
                            },
                            {
                                "project_announced_name": "游戏及其他",
                                "prime_operating_income": 63316334.3,
                                "income_ratio": 0.0343,
                                "gross_profit_rate": null
                            },
                            {
                                "project_announced_name": "电视剧",
                                "prime_operating_income": 50505855.6,
                                "income_ratio": 0.0274,
                                "gross_profit_rate": null
                            }
                        ]
                    },
                    {
                        "class_standard": 3,
                        "business_list": [
                            {
                                "project_announced_name": "华北地区",
                                "prime_operating_income": 1649889742.63,
                                "income_ratio": 0.895,
                                "gross_profit_rate": 0.5114414396715438
                            },
                            {
                                "project_announced_name": "华东地区",
                                "prime_operating_income": 71027506.05,
                                "income_ratio": 0.0385,
                                "gross_profit_rate": null
                            },
                            {
                                "project_announced_name": "华南地区",
                                "prime_operating_income": 62321110.18,
                                "income_ratio": 0.0338,
                                "gross_profit_rate": null
                            },
                            {
                                "project_announced_name": "其他收入之和",
                                "prime_operating_income": 60214402.19,
                                "income_ratio": 0.0327,
                                "gross_profit_rate": null
                            }
                        ]
                    }
                ]
            },
            ...
        ],
        "currency_code": "人民币"
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 十大股东

```python
import pysnowball as ball
ball.top_holders('SZ300251')
# or
ball.top_holders(symbol='SZ300251',circula=0)
```

输入参数：

* symbol -> 股票代码
* circula -> 只获取流通股,默认为1

结果显示：

```json
{
    "data": {
        "times": [
            {
                "name": "2018三季报",
                "value": 1538236800000
            },
            {
                "name": "2018中报",
                "value": 1530288000000
            },
            {
                "name": "2018一季报",
                "value": 1522425600000
            },
            {
                "name": "2017年报",
                "value": 1514649600000
            }
        ],
        "items": [
            {
                "chg": 133.92,
                "held_num": 763106985,
                "held_ratio": 10.96,
                "holder_name": "香港中央结算有限公司"
            },
            {
                "chg": 0,
                "held_num": 406609165,
                "held_ratio": 5.84,
                "holder_name": "Power Star Holdings(Hong Kong)Limited"
            },
            {
                "chg": -0.74,
                "held_num": 367792435,
                "held_ratio": 5.28,
                "holder_name": "Glossy City(HK)Limited"
            },
            {
                "chg": 0,
                "held_num": 259994273,
                "held_ratio": 3.73,
                "holder_name": "关玉婵"
            },
            {
                "chg": 0,
                "held_num": 247236384,
                "held_ratio": 3.55,
                "holder_name": "Gio2 Hong Kong Holdings Limited"
            },
            {
                "chg": 0,
                "held_num": 150837758,
                "held_ratio": 2.17,
                "holder_name": "Giovanna Investment Hong Kong Limited"
            },
            {
                "chg": -48.51,
                "held_num": 89849744,
                "held_ratio": 1.29,
                "holder_name": "易贤忠"
            },
            {
                "chg": -17.67,
                "held_num": 83437464,
                "held_ratio": 1.2,
                "holder_name": "全国社保基金四一三组合"
            },
            {
                "chg": null,
                "held_num": 72810935,
                "held_ratio": 1.05,
                "holder_name": "全国社保基金四一四组合"
            },
            {
                "chg": null,
                "held_num": 57580177,
                "held_ratio": 0.83,
                "holder_name": "挪威中央银行-自有资金"
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 主要指标

```python
import pysnowball as ball
ball.main_indicator('SZ300251')
```

输入参数：

* symbol -> 股票代码

结果显示：

```json
{
    "data": {
        "items": [
            {
                "asset_liab_ratio": 25.8594,
                "net_profit_atsopc_yoy": 22.8065,
                "operating_income_yoy": 24.5947,
                "basic_eps": 0.3277,
                "net_selling_rate": 44.0267,
                "avg_roe": 40.2459,
                "gross_selling_rate": 69.2402,
                "float_shares": 6964888862,
                "pb": 6.826,
                "np_per_share": 0.9217,
                "float_market_capital": 43739502053,
                "total_revenue": 10876591720.34,
                "market_capital": 92177088158,
                "pe_ttm": 13.363,
                "dividend": 0.083,
                "currency": "CNY",
                "dividend_yield": 1.322,
                "net_profit_atsopc": 4809760827.29,
                "total_shares": 14677880280,
                "report_date": "2018三季报"
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 股东人数

```python
import pysnowball as ball
ball.holders('SZ002027')
```

输入参数：

* symbol -> 股票代码

结果显示：

```json
{
    "data": {
        "items": [
            {
                "chg": 70.34,
                "price": 8.51,
                "ashare_holder": 134296,
                "timestamp": 1538236800000
            },
            {
                "chg": 12.68,
                "price": 9.57,
                "ashare_holder": 78838,
                "timestamp": 1530288000000
            },
            {
                "chg": 26.9,
                "price": 10.6423,
                "ashare_holder": 69964,
                "timestamp": 1522425600000
            },
            {
                "chg": -0.69,
                "price": 11.6248,
                "ashare_holder": 55132,
                "timestamp": 1514649600000
            },
            {
                "chg": -5.17,
                "price": 8.2976,
                "ashare_holder": 55515,
                "timestamp": 1506700800000
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 机构持仓

```python
import pysnowball as ball
ball.org_holding_change('SZ002027')
```

输入参数：

* symbol -> 股票代码

结果显示：

```json
{
    "data": {
        "items": [
            {
                "chg_date": "2018三季报",
                "institution_num": "202",
                "chg": -8.55,
                "held_ratio": 46.7108,
                "price": 8.51,
                "timestamp": 1538236800000
            },
            {
                "chg_date": "2018中报",
                "institution_num": "726",
                "chg": 5.68,
                "held_ratio": 55.2636,
                "price": 9.57,
                "timestamp": 1530288000000
            },
            {
                "chg_date": "2018一季报",
                "institution_num": "257",
                "chg": -12.08,
                "held_ratio": 49.5791,
                "price": 10.6423,
                "timestamp": 1522425600000
            },
            {
                "chg_date": "2017年报",
                "institution_num": "631",
                "chg": 4.75,
                "held_ratio": 61.6559,
                "price": 11.6248,
                "timestamp": 1514649600000
            },
            {
                "chg_date": "2017三季报",
                "institution_num": "119",
                "chg": -10.52,
                "held_ratio": 56.9054,
                "price": 8.2976,
                "timestamp": 1506700800000
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 分红融资

```python
import pysnowball as ball
ball.bonus('SZ002027')
```

输入参数：

* symbol -> 股票代码
* page -> 第几页 默认1
* size -> 每页含有多少数据 默认10

结果显示：

```json
{
    "data": {
        "addtions": [
            {
                "actual_issue_vol": 252525252,
                "actual_issue_price": 19.8,
                "listing_ad": 1460563200000,
                "actual_rc_net_amt": 4860797464
            },
            {
                "actual_issue_vol": 3813556382,
                "actual_issue_price": 10.46,
                "listing_ad": 1451232000000,
                "actual_rc_net_amt": 39889800000
            }
        ],
        "allots": [],
        "items": [
            {
                "dividend_year": "2018中报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2017年报",
                "ashare_ex_dividend_date": 1530201600000,
                "plan_explain": "10转2股派1元(含税)",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2017中报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2016年报",
                "ashare_ex_dividend_date": 1499270400000,
                "plan_explain": "10转4股派4.08元(含税)",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2016中报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2015年报",
                "ashare_ex_dividend_date": 1467216000000,
                "plan_explain": "10转10股派2.5元(含税)",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2015中报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2014年报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2014中报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            },
            {
                "dividend_year": "2013年报",
                "ashare_ex_dividend_date": null,
                "plan_explain": "不分配不转增",
                "cancle_dividend_date": null
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### F10 行业对比

```python
import pysnowball as ball
ball.industry_compare('SZ002027')
```

输入参数：

* symbol -> 股票代码

结果显示：

```json
{
    "data": {
        "ind_name": "营销服务",
        "quote_time": 1541487843000,
        "avg": {
            "pe_ttm": 18.075806451612905,
            "basic_eps": 0.14168064516129034,
            "avg_roe": 5.092969999999999,
            "gross_selling_rate": 19.05175483870968,
            "total_revenue": 3573300766.253226,
            "net_profit_atsopc": 266114972.18451613,
            "np_per_share": 4.066348387096774,
            "operate_cash_flow_ps": 0.0033032258064516146,
            "total_assets": 5442324297.112904,
            "total_shares": 1270069773.387097
        },
        "min": {
            "pe_ttm": -72.467,
            "basic_eps": -1.68,
            "avg_roe": -14.8514,
            "gross_selling_rate": -73.3425,
            "total_revenue": 105006980.06,
            "net_profit_atsopc": -497734761.09,
            "np_per_share": -1.6479,
            "operate_cash_flow_ps": -1.6162,
            "total_assets": 571320095.1,
            "total_shares": 93338000
        },
        "max": {
            "pe_ttm": 90.347,
            "basic_eps": 0.53,
            "avg_roe": 40.2459,
            "gross_selling_rate": 69.2402,
            "total_revenue": 17002184291.88,
            "net_profit_atsopc": 4809760827.29,
            "np_per_share": 10.3348,
            "operate_cash_flow_ps": 0.7028,
            "total_assets": 18485532791.55,
            "total_shares": 14677880280
        },
        "count": 1,
        "ind_code": "S720201",
        "ind_class": "SW2014",
        "report_name": "2018三季报",
        "items": [
            {
                "symbol": "SZ002027",
                "name": "分众传媒",
                "basic_eps": 0.3277,
                "total_revenue": 10876591720.34,
                "gross_selling_rate": 69.2402,
                "net_profit_atsopc": 4809760827.29,
                "np_per_share": 0.9217,
                "avg_roe": 40.2459,
                "pe_ttm": 13.363,
                "total_assets": 18485532791.55,
                "operate_cash_flow_ps": 0.1063,
                "total_shares": 14677880280
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### user 自选列表

```python
import pysnowball as ball
ball.watch_list()
```

结果显示：

```json
{
    "data": {
        "cubes": [
            {
                "id": -120,
                "name": "全部",
                "order_id": -50,
                "category": 3,
                "include": false,
                "symbol_count": 9,
                "type": -1
            },
            {
                "id": -27,
                "name": "沪深",
                "order_id": -40,
                "category": 3,
                "include": false,
                "symbol_count": 9,
                "type": -1
            },
            {
                "id": -26,
                "name": "港股",
                "order_id": -30,
                "category": 3,
                "include": false,
                "symbol_count": 0,
                "type": -1
            },
            {
                "id": -25,
                "name": "美股",
                "order_id": -20,
                "category": 3,
                "include": false,
                "symbol_count": 0,
                "type": -1
            },
            {
                "id": -24,
                "name": "我的",
                "order_id": -10,
                "category": 3,
                "include": false,
                "symbol_count": 4,
                "type": -1
            },
            {
                "id": -23,
                "name": "基金",
                "order_id": -7,
                "category": 3,
                "include": false,
                "symbol_count": 0,
                "type": -1
            }
        ],
        "funds": [
            {
                "id": -110,
                "name": "全部",
                "order_id": -30,
                "category": 2,
                "include": false,
                "symbol_count": 1,
                "type": -1
            },
            {
                "id": -17,
                "name": "基金",
                "order_id": -20,
                "category": 2,
                "include": false,
                "symbol_count": 1,
                "type": -1
            },
            {
                "id": -16,
                "name": "私募",
                "order_id": -10,
                "category": 2,
                "include": false,
                "symbol_count": 0,
                "type": -1
            }
        ],
        "stocks": [
            {
                "id": -1,
                "name": "全部",
                "order_id": 1,
                "category": 1,
                "include": false,
                "symbol_count": 76,
                "type": -1,
                "created_at": 1623925441286,
                "updated_at": 1623925441286
            },
            {
                "id": -5,
                "name": "沪深",
                "order_id": 7,
                "category": 1,
                "include": false,
                "symbol_count": 72,
                "type": -1,
                "created_at": 1623925441301,
                "updated_at": 1623925441301
            },
            {
                "id": -7,
                "name": "港股",
                "order_id": 8,
                "category": 1,
                "include": false,
                "symbol_count": 3,
                "type": -1,
                "created_at": 1623925441303,
                "updated_at": 1623925441303
            },
            {
                "id": -6,
                "name": "美股",
                "order_id": 9,
                "category": 1,
                "include": false,
                "symbol_count": 1,
                "type": -1,
                "created_at": 1623925441304,
                "updated_at": 1623925441304
            }
        ],
        "mutualFunds": [
            {
                "id": -160,
                "name": "全部",
                "order_id": -90,
                "category": 6,
                "include": false,
                "symbol_count": 0,
                "type": -1
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### user 自选列表详情

```python
import pysnowball as ball
ball.watch_stock(-1)
```

结果显示：

```json
{
    "data": {
        "pid": -5,
        "category": 1,
        "stocks": [
            {
                "symbol": "SH600809",
                "name": "山西汾酒",
                "type": 11,
                "remark": "",
                "exchange": "SH",
                "created": 1634611075047
            },
            {
                "symbol": "SH515790",
                "name": "光伏ETF",
                "type": 13,
                "remark": "",
                "exchange": "SH",
                "created": 1631856440323
            }
            {
                "symbol": "SH600030",
                "name": "中信证券",
                "type": 11,
                "remark": "",
                "exchange": "SH",
                "created": 1631601724976
            },
            {
                "symbol": "SH513050",
                "name": "中概互联网ETF",
                "type": 13,
                "remark": "",
                "exchange": "SH",
                "created": 1631195427798
            }
        ]
    },
    "error_code": 0,
    "error_description": ""
}
```

### cube 组合净值

```python
import pysnowball as ball
ball.nav_daily("ZH2567925")
```

结果显示：

```json
[
    {
        "symbol": "ZH2567925",
        "name": "混合",
        "list": [
            {
                "time": 1634486400000,
                "date": "2021-10-18",
                "value": 1.0299,
                "percent": 2.99
            },
            {
                "time": 1634572800000,
                "date": "2021-10-19",
                "value": 1.041,
                "percent": 4.1
            },
            {
                "time": 1634659200000,
                "date": "2021-10-20",
                "value": 1.044,
                "percent": 4.4
            }
        ]
    },
    {
        "symbol": "SH000300",
        "name": "沪深300",
        "list": [
            {
                "time": 1634486400000,
                "date": "2021-10-18",
                "value": 4874.78,
                "percent": -7.53
            },
            {
                "time": 1634572800000,
                "date": "2021-10-19",
                "value": 4922.72,
                "percent": -6.62
            },
            {
                "time": 1634659200000,
                "date": "2021-10-20",
                "value": 4910.18,
                "percent": -6.86
            }
        ]
    }
]
```

### cube 组合历史交易信息

```python
import pysnowball as ball
ball.rebalancing_history("ZH2567925")
```

结果显示：

```json
{
    "count": 20,
    "page": 1,
    "totalCount": 1,
    "list": [
        {
            "id": 106913130,
            "status": "success",
            "cube_id": 2601938,
            "prev_bebalancing_id": 103178834,
            "category": "user_rebalancing",
            "exe_strategy": "intraday_all",
            "created_at": 1634011887500,
            "updated_at": 1634014841878,
            "cash": 0.0,
            "error_code": null,
            "cash_value": 4.0E-7,
            "error_message": null,
            "error_status": null,
            "holdings": null,
            "rebalancing_histories": [
                {
                    "id": 235622410,
                    "rebalancing_id": 106913130,
                    "stock_id": 1028473,
                    "stock_name": "周大生",
                    "stock_symbol": "SZ002867",
                    "volume": 0.01629757,
                    "price": 21.49,
                    "net_value": 0.3502,
                    "weight": 33.0,
                    "target_weight": 33.0,
                    "prev_weight": 50.0,
                    "prev_target_weight": 50.0,
                    "prev_weight_adjusted": 57.29,
                    "prev_volume": 0.02829157,
                    "prev_price": 18.74,
                    "prev_net_value": 0.53018402,
                    "proactive": true,
                    "created_at": 1634014841878,
                    "updated_at": 1634014841878,
                    "target_volume": 0.01629757,
                    "prev_target_volume": 0.02829157
                },
                {
                    "id": 235622411,
                    "rebalancing_id": 106913130,
                    "stock_id": 1055251,
                    "stock_name": "君实生物-U",
                    "stock_symbol": "SH688180",
                    "volume": 0.00632992,
                    "price": 55.33,
                    "net_value": 0.3502,
                    "weight": 33.0,
                    "target_weight": 33.0,
                    "prev_weight": 50.0,
                    "prev_target_weight": 50.0,
                    "prev_weight_adjusted": 42.71,
                    "prev_volume": 0.00819323,
                    "prev_price": 64.71,
                    "prev_net_value": 0.53018391,
                    "proactive": true,
                    "created_at": 1634014841878,
                    "updated_at": 1634014841878,
                    "target_volume": 0.00632992,
                    "prev_target_volume": 0.00819323
                },
                {
                    "id": 235622412,
                    "rebalancing_id": 106913130,
                    "stock_id": 1028063,
                    "stock_name": "中概互联网ETF",
                    "stock_symbol": "SH513050",
                    "volume": 0.240245,
                    "price": 1.502,
                    "net_value": 0.3608,
                    "weight": 34.0,
                    "target_weight": 34.0,
                    "prev_weight": null,
                    "prev_target_weight": null,
                    "prev_weight_adjusted": null,
                    "prev_volume": null,
                    "prev_price": null,
                    "prev_net_value": null,
                    "proactive": true,
                    "created_at": 1634014841878,
                    "updated_at": 1634014841878,
                    "target_volume": 0.240245,
                    "prev_target_volume": null
                }
            ],
            "comment": "",
            "diff": 0.0,
            "new_buy_count": 0
        }
    ],
    "maxPage": 1
}
```

### 可转债信息

```python
import pysnowball as ball
ball.convertible_bond(page_size=5, page_count=1)
```

结果显示：

```json
{
    "version": "03070d792787f2543f5e2128fd0533e5",
    "result": {
        "pages": 632,
        "data": [
            {
                "SECURITY_CODE": "113053",
                "SECUCODE": "113053.SH",
                "TRADE_MARKET": "CNSESH",
                "SECURITY_NAME_ABBR": "隆22转债",
                "DELIST_DATE": None,
                "LISTING_DATE": None,
                "CONVERT_STOCK_CODE": "601012",
                "BOND_EXPIRE": "6",
                "RATING": "AAA",
                "VALUE_DATE": "2022-01-05 00: 00: 00",
                "ISSUE_YEAR": "2022",
                "CEASE_DATE": "2028-01-04 00: 00: 00",
                "EXPIRE_DATE": "2028-01-05 00: 00: 00",
                "PAY_INTEREST_DAY": "01-05",
                "INTEREST_RATE_EXPLAIN": "第一年0.20%、第二年0.40%、第三年0.80%、第四年1.20%、第五年1.60%、第六年2.00%。",
                "BOND_COMBINE_CODE": "22270600001JZJ",
                "ACTUAL_ISSUE_SCALE": 70,
                "ISSUE_PRICE": 100,
                "REMARK": "本次发行的可转换公司债券给予公司原A股股东优先配售权。本次发行的隆22转债向发行人在股权登记日收市后登记在册的原A股股东实行优先配售,原股东优先配售后余额部分通过上交所交易系统发售。",
                "PAR_VALUE": 100,
                "ISSUE_OBJECT": "(1)向公司原股东优先配售:发行公告公布的股权登记日(即2022年1月4日,T-1日)收市后登记在册的公司所有股东。(2)网上发行:中华人民共和国境内持有上交所证券账户的自然人、法人、证券投资基金、符合法律规定的其他投资者等(国家法律、法规禁止者除外)。(3)本次发行的联合主承销商的自营账户不得参与本次申购。",
                "REDEEM_TYPE": None,
                "EXECUTE_REASON_HS": None,
                "NOTICE_DATE_HS": None,
                "NOTICE_DATE_SH": None,
                "EXECUTE_PRICE_HS": None,
                "EXECUTE_PRICE_SH": None,
                "RECORD_DATE_SH": None,
                "EXECUTE_START_DATESH": None,
                "EXECUTE_START_DATEHS": None,
                "EXECUTE_END_DATE": None,
                "CORRECODE": "783012",
                "CORRECODE_NAME_ABBR": "隆基发债",
                "PUBLIC_START_DATE": "2022-01-05 00: 00: 00",
                "CORRECODEO": "764012",
                "CORRECODE_NAME_ABBRO": "隆基配债",
                "BOND_START_DATE": "2022-01-07 00: 00: 00",
                "SECURITY_START_DATE": "2022-01-04 00: 00: 00",
                "SECURITY_SHORT_NAME": "隆基股份",
                "FIRST_PER_PREPLACING": 1.293,
                "ONLINE_GENERAL_AAU": 1000,
                "ONLINE_GENERAL_LWR": 0.02376563,
                "INITIAL_TRANSFER_PRICE": 82.65,
                "TRANSFER_END_DATE": "2028-01-04 00: 00: 00",
                "TRANSFER_START_DATE": "2022-07-11 00: 00: 00",
                "RESALE_CLAUSE": "(1)有条件回售条款本次发行的可转换公司债券最后两个计息年度,如果公司股票在任何连续三十个交易日的收盘价低于当期转股价格的70%时,可转换公司债券持有人有权将其持有的可转换公司债券全部或部分按债券面值加上当期应计利息的价格回售给公司。若在前述三十个交易日内发生过转股价格因发生送股票股利、转增股本、增发新股(不包括因本次发行的可转换公司债券转股而增加的股本)、配股以及派发现金股利等情况而调整的情形,则在调整前的交易日按调整前的转股价格和收盘价计算,在调整后的交易日按调整后的转股价格和收盘价计算。如果出现转股价格向下修正的情况,则上述三十个交易日须从转股价格调整之后的第一个交易日起重新计算。本次发行的可转换公司债券最后两个计息年度,可转换公司债券持有人在每年回售条件首次满足后可按上述约定条件行使回售权一次,若在首次满足回售条件而可转换公司债券持有人未在公司届时公告的回售申报期内申报并实施回售的,该计息年度不应再行使回售权,可转换公司债券持有人不能多次行使部分回售权。(2)附加回售条款若本次发行可转换公司债券募集资金运用的实施情况与公司在募集说明书中的承诺相比出现变化,且该变化被中国证监会认定为改变募集资金用途的,可转换公司债券持有人享有一次以面值加上当期应计利息的价格向公司回售其持有的全部或部分可转换公司债券的权利。在上述情形下,可转换公司债券持有人可以在回售申报期内进行回售,在回售申报期内不实施回售的,不应再行使附加回售权(当期应计利息的计算方式参见赎回条款的相关内容)。",
                "REDEEM_CLAUSE": "(1)到期赎回条款在本次发行的可转换公司债券期满后五个交易日内,公司将按债券面值的107%(含最后一期利息)的价格赎回未转股的可转换公司债券。(2)有条件赎回条款在本次发行的可转换公司债券转股期内,如果公司A股股票连续三十个交易日中至少有十五个交易日的收盘价不低于当期转股价格的130%(含130%),或本次发行的可转换公司债券未转股余额不足人民币3,
                000万元时,公司有权按照债券面值加当期应计利息的价格赎回全部或部分未转股的可转换公司债券。当期应计利息的计算公式为:IA=B×i×t/365。IA:指当期应计利息;B:指本次发行的可转换公司债券持有人持有的可转换公司债券票面总金额;i:指可转换公司债券当年票面利率;t:指计息天数,即从上一个付息日起至本计息年度赎回日止的实际日历天数(算头不算尾)。若在前述三十个交易日内发生过转股价格调整的情形,则在转股价格调整日前的交易日按调整前的转股价格和收盘价计算,在转股价格调整日及之后的交易日按调整后的转股价格和收盘价计算。", "PARTY_NAME": "联合资信评估股份有限公司", "CONVERT_STOCK_PRICE": 80.27, "TRANSFER_PRICE": 82.65, "TRANSFER_VALUE": 97.1204, "CURRENT_BOND_PRICE": "-", "TRANSFER_PREMIUM_RATIO": 2.96, "CONVERT_STOCK_PRICEHQ": None, "MARKET": None, "RESALE_TRIG_PRICE": 57.86, "REDEEM_TRIG_PRICE": 107.45, "PBV_RATIO": 9.44, "IB_START_DATE": "2022-01-05 00: 00: 00", "IB_END_DATE": "2023-01-04 00: 00: 00", "CASHFLOW_DATE": "2023-01-05 00: 00: 00", "COUPON_IR": 0.2, "PARAM_NAME": "交易所系统网上向社会公众投资者发行,交易所系统网上向原A股无限售股东优先配售", "ISSUE_TYPE": "1,
                4", "EXECUTE_REASON_SH": None, "PAYDAYNEW": "-05", "CURRENT_BOND_PRICENEW": 100
            }
        ],
        "count": 632
    },
    "success": True,
    "message": "ok",
    "code": 0
}
```

### 指数基本信息

具体指数编码可参照：<https://www.csindex.com.cn>

```python
import pysnowball as ball
ball.index_basic_info("399967") #中证军工指数
```

结果显示：

```json
{
    "code": "200",
    "msg": "Success",
    "data": {
        "indexFullNameCn": "中证军工指数",
        "indexShortNameCn": "中证军工",
        "indexFullNameEn": "CSI National Defense Industry Index",
        "indexShortNameEn": "CSI National Defense",
        "indexCode": "399967",
        "ric": ".CSI399967",
        "bloombergid": "CSI9967",
        "basicDate": "2004-12-31",
        "basicIndex": 1000.0,
        "publishDate": "2013-12-26",
        "publishChannelCn": "卫星",
        "publishChannelEn": "卫星",
        "consNumber": None,
        "adjFreqCn": "每半年",
        "adjFreqEn": "Semiannually",
        "currencyCn": "人民币",
        "currencyEn": "CNY",
        "indexType": "stock",
        "indexCnDesc": "中证军工指数从沪深市场中选取十大军工集团控股的且主营业务与军工行业相关的上市公司证券，以及其他主营业务为军工行业的代表性上市公司证券作为指数样本，以反映军工行业公司的整体表现。",
        "indexEnDesc": "CSI National Defense Industry Index is designed to track the performance of national defense industry stocks. The Index consists of the companies which are controlled by the 10 largest military group corporations or operating in the national defense industry.       ",
        "weightingType": None,
        "weightingTypeEn": None,
        "ifWeightCapped": None,
        "ifWeightCappedEn": None,
        "indexCompliance": None
    },
    "success": True
}
```

### 指数详细信息

具体指数编码可参照：<https://www.csindex.com.cn>

```python
import pysnowball as ball
ball.index_details_data("399967") #中证军工指数
```

结果显示：

```json
{
    "code": "200",
    "msg": "Success",
    "data": {
        "编制方案": [
            {
                "fileName": "313_399967_Index_Methodology_en.pdf",
                "filePath": "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/indices/detail/files/en/313_399967_Index_Methodology_en.pdf",
                "fileType": "pdf"
            }
        ],
        "发行人名单": None,
        "备选名单": None,
        "指数单张": [
            {
                "fileName": "399967factsheeten.pdf",
                "filePath": "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/indices/detail/files/en/399967factsheeten.pdf",
                "fileType": "pdf"
            },
            {
                "fileName": "H20229factsheet.pdf",
                "filePath": "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/indices/detail/files/en/H20229factsheet.pdf",
                "fileType": "pdf"
            }
        ],
        "样本权重": [
            {
                "fileName": "399967closeweight",
                "filePath": "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/closeweight/399967closeweight.xls",
                "fileType": "xls"
            }
        ],
        "样本列表": [
            {
                "fileName": "399967cons",
                "filePath": "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/cons/399967cons.xls",
                "fileType": "xls"
            }
        ],
        "指数估值": [
            {
                "fileName": "399967indicator",
                "filePath": "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/indicator/399967indicator.xls",
                "fileType": "xls"
            }
        ]
    },
    "success": True
}
```

### 指数权重股前十

具体指数编码可参照：<https://www.csindex.com.cn>

```python
import pysnowball as ball
ball.index_weight_top10("399967") #中证军工指数
```

结果显示：

```json
{
    "code": "200",
    "msg": "Success",
    "data": {
        "updateDate": "2022-01-07",
        "top5Sum": 27.35,
        "top10Sum": 41.98,
        "weightList": [
            {
                "rowNum": "1",
                "indexCode": "399967",
                "tradeDate": "20220107",
                "securityCode": "002049",
                "securityName": "紫光国微",
                "securityNameEn": "Unigroup Guoxin Microelectronics Co., Ltd.",
                "csiTypeL1": "信息技术",
                "csiTypeL1En": "Information Technology",
                "marketNameCn": "深圳证券交易所",
                "marketNameEn": "Shenzhen  Exchange",
                "weight": 7.92,
                "preciseWeight": 7.9236710279527784
            },
            {
                "rowNum": "2",
                "indexCode": "399967",
                "tradeDate": "20220107",
                "securityCode": "600893",
                "securityName": "航发动力",
                "securityNameEn": "AVIC AVIATION ENGINE CORPORATION PLC.",
                "csiTypeL1": "工业",
                "csiTypeL1En": "Industrials",
                "marketNameCn": "上海证券交易所",
                "marketNameEn": "Shanghai  Exchange",
                "weight": 6.62,
                "preciseWeight": 6.620251010156067
            },
            {
                "rowNum": "3",
                "indexCode": "399967",
                "tradeDate": "20220107",
                "securityCode": "002179",
                "securityName": "中航光电",
                "securityNameEn": "AVIC Jonhon Optronic Technology Co.,Ltd.",
                "csiTypeL1": "工业",
                "csiTypeL1En": "Industrials",
                "marketNameCn": "深圳证券交易所",
                "marketNameEn": "Shenzhen  Exchange",
                "weight": 4.5,
                "preciseWeight": 4.502779273316449
            },
            {
                "rowNum": "4",
                "indexCode": "399967",
                "tradeDate": "20220107",
                "securityCode": "601989",
                "securityName": "中国重工",
                "securityNameEn": "China Shipbuilding Industry Co Ltd",
                "csiTypeL1": "工业",
                "csiTypeL1En": "Industrials",
                "marketNameCn": "上海证券交易所",
                "marketNameEn": "Shanghai  Exchange",
                "weight": 4.28,
                "preciseWeight": 4.284116029624741
            },
            {
                "rowNum": "5",
                "indexCode": "399967",
                "tradeDate": "20220107",
                "securityCode": "000768",
                "securityName": "中航西飞",
                "securityNameEn": "AVIC XI'AN AIRCRAFT INDUSTRY GROUP COMPANY LTD.",
                "csiTypeL1": "工业",
                "csiTypeL1En": "Industrials",
                "marketNameCn": "深圳证券交易所",
                "marketNameEn": "Shenzhen  Exchange",
                "weight": 4.02,
                "preciseWeight": 4.020696936529087
            },
            {
                "rowNum": "6",
                "indexCode": "399967",
                "tradeDate": "20220107",
                "securityCode": "000733",
                "securityName": "振华科技",
                "securityNameEn": "China Zhenhua (Group) Science & Technology Co Ltd",
                "csiTypeL1": "信息技术",
                "csiTypeL1En": "Information Technology",
                "marketNameCn": "深圳证券交易所",
                "marketNameEn": "Shenzhen  Exchange",
                "weight": 3.73,
                "preciseWeight": 3.7268720605305283
            },
            {
                "rowNum": "7",
                "indexCode": "399967",
                "tradeDate": "20220107",
                "securityCode": "600760",
                "securityName": "中航沈飞",
                "securityNameEn": "AVIC SHENYANG AIRCRAFT COMPANY LIMITED",
                "csiTypeL1": "工业",
                "csiTypeL1En": "Industrials",
                "marketNameCn": "上海证券交易所",
                "marketNameEn": "Shanghai  Exchange",
                "weight": 3.23,
                "preciseWeight": 3.229894039999866
            },
            {
                "rowNum": "8",
                "indexCode": "399967",
                "tradeDate": "20220107",
                "securityCode": "002013",
                "securityName": "中航机电",
                "securityNameEn": "AVIC Electromechanical Systems Co., Ltd.",
                "csiTypeL1": "工业",
                "csiTypeL1En": "Industrials",
                "marketNameCn": "深圳证券交易所",
                "marketNameEn": "Shenzhen  Exchange",
                "weight": 2.77,
                "preciseWeight": 2.773592431150194
            },
            {
                "rowNum": "9",
                "indexCode": "399967",
                "tradeDate": "20220107",
                "securityCode": "600765",
                "securityName": "中航重机",
                "securityNameEn": "Avic Heavy Machinery Co Ltd",
                "csiTypeL1": "工业",
                "csiTypeL1En": "Industrials",
                "marketNameCn": "上海证券交易所",
                "marketNameEn": "Shanghai  Exchange",
                "weight": 2.46,
                "preciseWeight": 2.4619565694074566
            },
            {
                "rowNum": "10",
                "indexCode": "399967",
                "tradeDate": "20220107",
                "securityCode": "002268",
                "securityName": "卫士通",
                "securityNameEn": "Westone Information Industry Inc",
                "csiTypeL1": "信息技术",
                "csiTypeL1En": "Information Technology",
                "marketNameCn": "深圳证券交易所",
                "marketNameEn": "Shenzhen  Exchange",
                "weight": 2.44,
                "preciseWeight": 2.4397637345969736
            }
        ]
    },
    "success": True
}
```

### 指数收益

具体指数编码可参照：<https://www.csindex.com.cn>

```python
import pysnowball as ball
ball.index_perf_7("399967") #最近7天数据
ball.index_perf_30("399967") #最近30天数据
ball.index_perf_90("399967") #最近90天数据
```

结果显示：

```json
{
    "code": "200",
    "msg": "Success",
    "data": [
        {
            "tradeDate": "20220104",
            "indexCode": "399967",
            "indexNameCnAll": "中证军工指数",
            "indexNameCn": "中证军工",
            "indexNameEnAll": "CSI National Defense Industry Index",
            "indexNameEn": "CSI National Defense",
            "open": 14894.07,
            "high": 14972.07,
            "low": 14631.92,
            "close": 14732.88,
            "change": -164.01,
            "changePct": -1.1,
            "tradingVol": 10.21,
            "tradingValue": 306.36,
            "consNumber": 64.0
        },
        {
            "tradeDate": "20220105",
            "indexCode": "399967",
            "indexNameCnAll": "中证军工指数",
            "indexNameCn": "中证军工",
            "indexNameEnAll": "CSI National Defense Industry Index",
            "indexNameEn": "CSI National Defense",
            "open": 14690.36,
            "high": 14750.57,
            "low": 13958.84,
            "close": 13979.6,
            "change": -753.28,
            "changePct": -5.11,
            "tradingVol": 11.73,
            "tradingValue": 361.02,
            "consNumber": 64.0
        },
        {
            "tradeDate": "20220106",
            "indexCode": "399967",
            "indexNameCnAll": "中证军工指数",
            "indexNameCn": "中证军工",
            "indexNameEnAll": "CSI National Defense Industry Index",
            "indexNameEn": "CSI National Defense",
            "open": 13902.36,
            "high": 13983.25,
            "low": 13664.19,
            "close": 13805.97,
            "change": -173.63,
            "changePct": -1.24,
            "tradingVol": 9.02,
            "tradingValue": 277.33,
            "consNumber": 64.0
        },
        {
            "tradeDate": "20220107",
            "indexCode": "399967",
            "indexNameCnAll": "中证军工指数",
            "indexNameCn": "中证军工",
            "indexNameEnAll": "CSI National Defense Industry Index",
            "indexNameEn": "CSI National Defense",
            "open": 13834.46,
            "high": 13928.36,
            "low": 13605.02,
            "close": 13614.24,
            "change": -191.73,
            "changePct": -1.39,
            "tradingVol": 8.5,
            "tradingValue": 231.62,
            "consNumber": 64.0
        }
    ],
    "success": True
}
```

### 深港通 北向数据 STOCK CONNECT NORTHBOUND SHAREHOLDING SEARCH BY DATE

> 可参照：<https://www.hkexnews.hk/sdw/search/mutualmarket.aspx?t=sz>

```python
import pysnowball as ball
ball.northbound_shareholding_sh() #默认当天
ball.northbound_shareholding_sh('2022/01/19')
```

结果显示：

```json
[
    {
        "code": "30002", 
        "name": "RAYTRON TECHNOLOGY CO.,LTD. (A #688002)", 
        "shareholding": 6241840, 
        "shareholding_percent": "2.43%"
    },
    ...
]
```

### 沪港通 北向数据 STOCK CONNECT NORTHBOUND SHAREHOLDING SEARCH BY DATE

> 可参照：<https://www.hkexnews.hk/sdw/search/mutualmarket.aspx?t=sh>

```python
import pysnowball as ball
data = ball.northbound_shareholding_sz() #默认当天 可选填日期-格式：'2022/01/19'
print(data[0])
```

结果显示：

```json
{
    "code": "70001", 
    "name": "PING AN BANK CO., LTD. (A #000001)", 
    "shareholding": 1839598842, 
    "shareholding_percent": "9.47%"
}
```

### fund


#### fund_detail

```python
import pysnowball as ball
ball.fund_detail("008975")
```

[结果显示](APIs/fund_detail.md)

#### fund_info

```python
import pysnowball as ball

ball.fund_info("008975")
```

[结果显示](APIs/fund_info.md)


#### fund_growth

```python
import pysnowball as ball
ball.fund_growth("008975")
```

[结果显示](APIs/fund_growth.md)



#### fund_nav_history

```python
import pysnowball as ball
ball.fund_nav_history("008975")
```

[结果显示](APIs/fund_nav_history.md)


#### fund_achievement

```python
import pysnowball as ball
ball.fund_achievement("008975")
```

[结果显示](APIs/fund_achievement.md)


#### fund_asset

```python
import pysnowball as ball
ball.fund_asset("008975")
```

[结果显示](APIs/fund_asset.md)


#### fund_manager

```python
import pysnowball as ball
ball.fund_manager("008975")
```

[结果显示](APIs/fund_manager.md)


#### fund_trade_date

```python
import pysnowball as ball
ball.fund_trade_date("008975")
```

[结果显示](APIs/fund_trade_date.md)


#### fund_derived

```python
import pysnowball as ball
ball.fund_derived("008975")
```

[结果显示](APIs/fund_derived.md)
