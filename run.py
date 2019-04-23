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
    cache_name='cache',
    backend='sqlite',
    expire_after=expire_after,
)

STOCKS = {
    'fuYao': "600660.ss"
}


def get_px(stock, start, end):
    return web.DataReader(stock, 'yahoo', start, end, session=session)


if __name__ == "__main__":
    start = datetime(2010, 1, 1)
    today = datetime.today()

    for (k, v) in STOCKS.items():
        px = DataFrame(get_px(v, start, today))

    # print(pdr.get_quote_yahoo(STOCKS['fuYao']))

# fuYao["Adj Close"].plot(legend=True)
#
# pyplot.show()
