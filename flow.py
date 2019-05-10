import my_tushare as ts
from matplotlib import pyplot
from pandas import Series, DataFrame
from datetime import datetime, timedelta

# 设置token
token = '3af5b0a6e8922ba964ac5590bd3718503de6c5a9b4fef775e6e32553'
pro = ts.pro_api(token)


# 单位百万
def get_flow():
    return DataFrame(pro.moneyflow_hsgt(start_date='20190401', end_date='20190430'))


if __name__ == "__main__":
    dataDf = get_flow()['north_money']
    print(dataDf)
    # 单位亿
    dataDf = dataDf.apply(lambda x: x / 100)
    dataDf = dataDf.cumsum()
    dataDf.plot(legend=True)
    pyplot.show()
