import json
import urllib
import twder


# https://medium.com/marketingdatascience/%E7%84%A1%E9%A0%88%E5%AF%AB%E7%88%AC%E8%9F%B2-%E9%A6%AC%E4%B8%8A%E5%B9%AB%E6%82%A8%E7%88%AC%E5%8F%96%E5%8C%AF%E7%8E%87-%E6%8E%8C%E6%8E%A7%E6%9C%80%E6%96%B0%E8%B2%BF%E6%98%93%E5%8C%AF%E6%90%8D-%E9%99%84%E4%B8%8Apython-%E7%A8%8B%E5%BC%8F%E7%A2%BC-d3da7a8209f0

# 查询所有货币代号
def get_currencies():
    return twder.currencies()


# 格式：{货币代码: (时间, 现金买入, 现金卖出, 即期买入, 即期卖出)}
# 例：‘USD’: (‘2018/10/18 16:00’, ‘30.53’, ‘31.22’, ‘30.9’, ‘31’)
def get_all():
    return twder.now_all()


# 查询人民币汇率：当前
def get_cny():
    return float(twder.now('USD')[1]) / float(twder.now('CNY')[1])


# 查询人民币汇率：过去6个月
def get_past_six_month_cny():
    return twder.past_six_month('CNY')


if __name__ == "__main__":
    print(get_cny())
