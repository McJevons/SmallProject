# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:37:12 2019

@author: McJevons
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('F:/jupyter notebook/SmallProject/lianjia.csv')
data.head(2)

# 查找哪列存在缺失值
data.isnull().any()
data.info()


# 查看数据概述，大致了解是否存在异常值
data_desc=data.describe()


# 增加单价列
data['avgprice']=data['Price']/data['Size']
data.drop('avrprice',axis=1,inplace=True)

# 修改列名
col_cn=['朝向','板块','电梯','楼层','小区','Id','房型','总价','区','装修','面积','年份','单价']
data.rename(dict(zip(list(data.columns),col_cn)),axis=1,inplace=True)
data=pd.DataFrame(data,columns=['区','板块','朝向','楼层','单价','面积','总价','电梯','房型','装修','花园','年份'])
data.rename({'花园':'小区'},axis=1,inplace=True)

# 处理缺失值
data['电梯'].fillna('无电梯',inplace=True)

