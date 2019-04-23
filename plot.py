import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 股票数据读取
import pandas_datareader as pdr

# 可视化
import matplotlib as plt
from matplotlib import pyplot

import seaborn as sns

from datetime import datetime

radius = [1.0, 2.0, 3.0, 4.0]
area = [3.14159, 12.56636, 28.27431, 50.26544]

pyplot.plot(radius, area)
pyplot.show()
