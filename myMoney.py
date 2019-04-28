# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

data=pd.read_excel('F:/jupyter notebook/SmallProject/myMoney.xls',sheet_name='支出')

data.columns

data=data.reindex(columns=['类别', '子类', '账户1', '花费', '日期', '详细'])

data.fillna('--',inplace=True)

data.groupby('类别').sum()

pd.to_datetime(data['日期']).apply(lambda x:[x.month,x.year,x.day])

data['date']=pd.to_datetime(data['日期'])
data.groupby(data['date'].apply(lambda x:x.year)).sum().hist()

data['year']=data['date'].apply(lambda x:x.year)
data['month']=data['date'].apply(lambda x:x.month)
data['day']=data['date'].apply(lambda x:x.day)

d=data.groupby(['year','month'])['花费'].sum()
plt.plot(d)
plt.show()
