# 上证指数和汇率的关系

from matplotlib import pyplot
from datetime import datetime

import currency_rate
import ss

if __name__ == "__main__":
    start = datetime(2010, 1, 1)
    today = datetime.today()

    ssDf = ss.get_ss(start, today)
    rateDf = currency_rate.get_cny(start, today)

    rateDf = rateDf.apply(lambda x: (x - 6) * 3000)

    # 画纸
    ax1 = ssDf.plot(y="ss", label="ss", legend=True)

    rateDf.plot(ax=ax1, label="rate", legend=True)

    pyplot.xlabel('date')

    pyplot.ylabel('ss/currency')
    pyplot.title('ss VS currency rate')
    pyplot.grid(True)
    pyplot.show()
