# 上证指数

import requests_cache

# 股票数据读取
import pandas_datareader.data as web

# 可视化
from matplotlib import pyplot

import seaborn as sns

from datetime import datetime, timedelta

expire_after = timedelta(days=3)
session = requests_cache.CachedSession(
    cache_name='cache',
    backend='sqlite',
    expire_after=expire_after,
)


def get_ss(start=datetime(2018, 1, 1), end=datetime.today()):
    return web.DataReader("000001.SS", 'yahoo', start, end, session=session)


if __name__ == "__main__":
    df = get_ss()
    print(df)
    df["Close"].plot(legend=True)
    pyplot.show()
