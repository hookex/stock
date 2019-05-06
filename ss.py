# 上证指数

import requests_cache

# 股票数据读取
import pandas_datareader.data as web
from pandas import Series, DataFrame


# 可视化
from matplotlib import pyplot

from datetime import datetime, timedelta

expire_after = timedelta(days=3)
session = requests_cache.CachedSession(
    cache_name='cache',
    backend='sqlite',
    expire_after=expire_after,
)


def get_ss(start=datetime(2019, 4, 1), end=datetime.today()):
    return DataFrame(web.DataReader("000001.SS", 'yahoo', start, end, session=session))


if __name__ == "__main__":
    df = get_ss()["Adj Close"]
    print(df)
    df.plot()
    pyplot.show()
