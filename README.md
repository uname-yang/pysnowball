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

![img](https://blog.crackcreed.com/content/images/2017/11/qrcode_for_gh_ab3754053ff8_344.jpg)

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
