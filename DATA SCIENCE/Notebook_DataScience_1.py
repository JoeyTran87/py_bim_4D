#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas.core.series import Series




path_excel_memo = r"K:\_WFH VIETMY\XLSX\MEMORY.xlsx"
memo_df2 = pd.read_excel(path_excel_memo,sheet_name = "Sheet1",index_col=0).dropna()

dic = memo_df2.to_dict()["Memory Value"]
for d in dic:
    dic[d] = list(dic[d])
print(dic)

