# A股大盘指数和汇率的关系

import tushare as ts
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

from pylab import mpl

# K线图可视化
from pyecharts import Kline

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# 设置token
token = '3af5b0a6e8922ba964ac5590bd3718503de6c5a9b4fef775e6e32553'
# ts.set_token(token)
pro = ts.pro_api(token)

df = pro.index_dailybasic(trade_date='20181018', fields='ts_code,trade_date,turnover_rate,pe')

print(df)
