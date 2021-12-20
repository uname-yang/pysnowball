# -*- coding: utf-8 -*-

import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

long_desc = """
# pysnowball
===============

## quick start

```python
>>> import pysnowball as ball
>>> ball.set_token('xq_a_token=651af***************031c96a315c;')
'xq_a_token=651af***************031c96a315c;'
>>> ball.cash_flow('SH600000')
```

```json
{
    'data': {
        'quote_name': '浦发银行',
        'currency_name': '人民币',
        'org_type': 2,
        'last_report_name': '2018三季报',
        'currency': 'CNY',
        'list': [{
                    'report_date': 1514649600000,
                    'report_name': '2017年报',
                    'ncf_from_oa': [-140673000000.0, 0.26730141203064695],
                    'ncf_from_ia': [37800000000.0, 1.590486604702023],
                    'ncf_from_fa': [4820000000.0, -0.9794317706599756
                    ]
                }, {
                    'report_date': 1483113600000,
                    'report_name': '2016年报',
                    'ncf_from_oa': [-191993000000.0, -1.5350677219775932],
                    'ncf_from_ia': [-64015000000.0, 0.8794943714468582
                    ],
                    'ncf_from_fa': [234342000000.0, -0.042650194867269654]
                }, {
                    'report_date': 1451491200000,
                    'report_name': '2015年报',
                    'ncf_from_oa': [358820000000.0, 0.8770859707676373],
                    'ncf_from_ia': [-531220000000.0, -0.5512111080287921],
                    'ncf_from_fa': [244782000000.0, 2.357915963619902]
                }, {
                    'report_date': 1419955200000,
                    'report_name': '2014年报',
                    'ncf_from_oa': [191158000000.0, -0.3801741859756295],
                    'ncf_from_ia': [-342455000000.0, -0.08702069578466226],
                    'ncf_from_fa ': [72897000000.0, 4.966967784066173]
                },  {
                    'report_date ': 1388419200000,
                    'report_name ': '2013 年报 ',
                    'ncf_from_oa ': [308406000000.0, 2.3313098144267537], 
                    'ncf_from_ia ': [-315040000000.0, -1.2059925355889953],
                    'ncf_from_fa ': [-18376000000.0, -1.6123496284447998]
                }
            ]}, 
            'error_code ': 0, 
            'error_description': ''
        }
```
"""

def read_install_requires():
    reqs = [
        # 'pandas >= 0.23.4',
        'requests >= 2.18.4'
    ]
    return reqs

setuptools.setup(
    name="pysnowball",
    version="0.0.8",
    author="Yang Yu",
    author_email="yang.lights@hotmail.com",
    description="xueqiu api python client | 集成雪球API",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/uname-yang/pysnowball",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=('Financial Data','XueQiu','Snow Ball','雪球','Python Api'),
    install_requires=read_install_requires(),
)
