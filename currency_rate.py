# 获取历史汇率

import pandas_datareader.data as web
from pandas import DataFrame

import requests_cache

from matplotlib import pyplot
from datetime import datetime, timedelta

expire_after = timedelta(days=7)
session = requests_cache.CachedSession(
    cache_name='cache',
    backend='sqlite',
    expire_after=expire_after,
)


# 这个数据源的延迟太高
def get_cny(start=datetime(2019, 1, 1), end=datetime.today()):
    return DataFrame(web.get_data_fred('DEXCHUS', start, end, session=session))


if __name__ == "__main__":
    df = get_cny(datetime(2019, 4, 1))
    print(df)
    df.plot(legend=True)
    pyplot.show()
