import my_tushare as ts
from pandas import Series, DataFrame

# 设置token
token = '3af5b0a6e8922ba964ac5590bd3718503de6c5a9b4fef775e6e32553'
# ts.set_token(token)
pro = ts.pro_api(token)


# 所有股票列表
def get_all_stock_code():
    basic = pro.stock_basic(list_status='L')
    return DataFrame(basic, columns=['ts_code'])


# 上市公司基础信息
def get_stock_company():
    return pro.stock_company(
        exchange='SZSE',
        fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province'
    )


# 公司利润表
def get_income():
    df = pro.income(ts_code='600660.SH', start_date='20180101', end_date='20180730',
                    fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps')
    return df


# 财务指标数据
# https://tushare.pro/document/2?doc_id=79
def get_indicator():
    df = pro.query('fina_indicator', ts_code='600660.SH', start_date='20190101', end_date='20190505')
    return DataFrame(df)


if __name__ == "__main__":
    print(get_indicator())
