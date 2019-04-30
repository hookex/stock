# 获取历史汇率

import pandas_datareader.data as web

import requests_cache
from datetime import timedelta

from matplotlib import pyplot

import seaborn as sns

from datetime import datetime

radius = [1.0, 2.0, 3.0, 4.0]
area = [3.14159, 12.56636, 28.27431, 50.26544]

expire_after = timedelta(days=7)
session = requests_cache.CachedSession(
    cache_name='quote',
    backend='sqlite',
    expire_after=expire_after,
)


def get_cny():
    cny = web.get_data_fred('DEXCHUS', session=session)
    return cny


if __name__ == "__main__":
    get_cny().plot(legend=True)
    pyplot.show()
