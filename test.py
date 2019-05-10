import my_tushare as ts
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

from pylab import mpl
import config

# K线图可视化
from pyecharts import Kline

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# 设置token

# ts.set_token(token)
pro = ts.pro_api(config.token)

# fd = ts.Macro()
# df = fd.ChinaDataCPI(indicID='M030000003', field='indicName,periodDate,dataValue,dataSource')
# df = df.sort('periodDate', ascending=False)


print(ts.get_deposit_rate())


import K
K.token