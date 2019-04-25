import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import requests_cache

# 股票数据读取
import pandas_datareader as pdr
import pandas_datareader.data as web

# 可视化
import matplotlib as plt
from matplotlib import pyplot

import seaborn as sns

from datetime import datetime, timedelta

expire_after = timedelta(days=3)
session = requests_cache.CachedSession(
    cache_name='quote',
    backend='sqlite',
    expire_after=expire_after,
)

STOCKS = {
    'fuYao': '600660.ss',
    'haiKang': '002415.sz',
    'zhiHui': '600869.ss',
    # 'jingLan': '000711.sz',
}


def get_px(stock):
    return pdr.get_quote_yahoo(stock, session=session)


def get_px_error(stocks):
    return DataFrame({n: get_px(n) for n in stocks.values()})


def get_pxs(stocks):
    df = DataFrame()

    for stock in stocks.values():
        df = df.append(get_px(stock))

    return df


if __name__ == "__main__":
    px = get_pxs(STOCKS)

    # fields = ['shortName', 'price', 'forwardPE']

    print(px.to_json())
