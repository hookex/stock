# 上证指数和汇率的关系

import pandas as pd
from matplotlib import pyplot
from datetime import datetime

import currency_rate
import ss

if __name__ == "__main__":
    start = datetime(2018, 3, 1)
    today = datetime.today()
    index = pd.DataFrame(columns=['SS', 'CNYUSD'])

    ssDf = ss.get_ss(start, today)
    cn_us = currency_rate.get_cny(start, today).apply(lambda x: (1 / x))

    index['SS'] = ssDf["Adj Close"]
    index['CNYUSD'] = cn_us['DEXCHUS']

    index.plot(subplots=True, figsize=(16, 10), grid=True, x_compat=True)

    pyplot.title('ss VS currency rate')
    pyplot.show()
