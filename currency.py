# 获取历史汇率

import pandas_datareader.data as web

import requests_cache
from datetime import timedelta

from matplotlib import pyplot

expire_after = timedelta(days=7)
session = requests_cache.CachedSession(
    cache_name='currency',
    backend='sqlite',
    expire_after=expire_after,
)


def get_cny():
    cny = web.get_data_fred('DEXCHUS', session=session)
    return cny


if __name__ == "__main__":
    get_cny().plot(legend=True)
    pyplot.show()
