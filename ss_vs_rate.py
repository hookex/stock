# 上证指数和汇率的关系

import pandas as pd
from matplotlib import pyplot
from datetime import datetime

import currency_rate
import ss
import gold

if __name__ == "__main__":
    start = datetime(2018, 3, 1)
    today = datetime.today()
    index = pd.DataFrame(columns=['SS', 'CNYUSD'])

    ss_df = ss.get_ss(start, today)
    gold_df = gold.get_gold(start, today)
    cn_us_df = currency_rate.get_cny(start, today).apply(lambda x: (1 / x))

    index['SS'] = ss_df["Adj Close"]
    index['CNYUSD'] = cn_us_df['DEXCHUS']
    index['Gold'] = gold_df['GOLDAMGBD228NLBM']

    index.plot(subplots=True, figsize=(16, 10), grid=True, x_compat=True)

    pyplot.title('ss VS currency rate')
    pyplot.show()
