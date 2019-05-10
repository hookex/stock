import my_tushare as ts
from pandas import Series, DataFrame

# 设置token
token = '3af5b0a6e8922ba964ac5590bd3718503de6c5a9b4fef775e6e32553'
# ts.set_token(token)
pro = ts.pro_api(token)


def get_all_stock_code():
    basic = pro.stock_basic(list_status='L')
    return DataFrame(basic, columns=['ts_code'])
