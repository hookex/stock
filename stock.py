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

from all_stock import get_all_stock_code

expire_after = timedelta(days=7)
session = requests_cache.CachedSession(
    cache_name='cache',
    backend='sqlite',
    expire_after=expire_after,
)

STOCKS = {
    'fuYao': '600660.ss',
    'haiKang': '002415.sz',
    'zhiHui': '600869.ss',
    'jingLan': '000711.sz',
}


def get_stock(stock):
    return DataFrame(pdr.get_quote_yahoo(stock, session=session))


def get_stock_quandl(stock):
    return DataFrame(pdr.get_data_quandl(stock, api_key="A83E-dJAdqmse9P-Tpng", session=session))


# TODO: 不能用
def get_px_error(stocks):
    return DataFrame({n: get_stock(n) for n in stocks.values()})


def get_pxs(stocks):
    df = DataFrame()

    for stock in stocks.values():
        df = df.append(get_stock(stock))

    return df


if __name__ == "__main__":
    all_stock_code_df = get_all_stock_code()

    for code in all_stock_code_df:
        print(code)

    px = get_pxs(STOCKS)

    columns = ['shortName', 'price', 'forwardPE']

    print(px.get(columns))
