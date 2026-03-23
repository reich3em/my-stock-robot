from Ashare import *
import pandas as pd

# 获取长江电力(600900)最近30个交易日数据
df = get_price('sh600900', frequency='1d', count=30)
print(df)
df.to_csv('stock_600900_30days.csv')
