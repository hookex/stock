import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import requests_cache

# 股票数据读取
import pandas_datareader as pdr
import pandas_datareader.data as web

# 可视化
import matplotlib as plt
from matplotlib import pyplot

import seaborn as sns

from datetime import datetime, timedelta

import stock

# 600660.ss

if __name__ == "__main__":
    stock = stock.get_stock_quandl("600660")

    print(stock.to_json())
