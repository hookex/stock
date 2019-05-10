import my_tushare as ts
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

# 获取当前上市的股票代码、简称、注册地、行业、上市时间等数据
basic = pro.stock_basic(list_status='L')
# 查看前五行数据
# basic.head(5)

# 获取日行情数据
pa = pro.daily(ts_code='000711.SZ', start_date='20180101',
               end_date='20190106')
# pa.head()

pa.index = pd.to_datetime(pa.trade_date)
pa = pa.sort_index()
v1 = list(pa.loc[:, ['open', 'close', 'low', 'high']].values)
t = pa.index
v0 = list(t.strftime('%Y%m%d'))
kline = Kline("K线图", title_text_size=15)
kline.add("", v0, v1, is_datazoom_show=True,
          mark_line=["average"],
          mark_point=["max", "min"],
          mark_point_symbolsize=60,
          mark_line_valuedim=['highest', 'lowest'])

kline.render("K线图.html")

kline
