from os import truncate
from typing import List
import pandas as pd
import main_naming_code
from main_naming_code import abserviation
 #----------------------------------------------------#  SETUP PANDAS
pd.set_option('display.max_rows', 0)
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 80)

file_path = r"F:\_NGHIEN CUU\_Github\py_bim_4D\XLSX\SS-03-TRACKING-210927.xlsx"

excel_file = pd.ExcelFile(file_path)# [print(shn) for shn in excel_file.sheet_names]

sheet_name = 'WorkItemData-TRACK'

df = pd.read_excel(excel_file,sheet_name)# print(df)

headers = df.columns# [print(hd) for hd in list(headers)]

header_key = 'Work Item Number'

data = df[header_key]# print(data)

data_list = [str(d).split("-") for d in data]# [print(d) for d in data_list]

data_level = [len(d) for d in data_list]# [print(d) for d in data_level]

dic_level = {} # tự điển các Level 
for d in data_level:
    dic_level[d] = []
for d in data_list:
    dic_level[len(d)].append(d)# [print(f"{d} : {dic_level[d]}") for d in dic_level]# [print(f"{d} : {len(dic_level[d])}") for d in dic_level]

dic_code = abserviation() # Tự điển tra cứu mã số -> Tên# [print(f"{d} : {dic_code[d]}") for d in dic_code]

dic_add = {} # tự điển các Mã CT Parent cần add thêm

for d in data_list:
    if len(d) > 1:
        parent = d[:-1]
        if not parent in dic_level[len(parent)]:
            dic_add["-".join(d[:-1])] = ""# [print(f"{d}") for d in dic_add]



for d in dic_add:
    codes = d.split("-")
    dic_add[d] = " ".join([dic_code[c] for c in codes if c in dic_code])# [print(f"{d}:{dic_add[d]}") for d in dic_add]

print(df.index)
[print(f"{d} : {df.iloc[2].to_dict()[d]}") for d in df.iloc[2].to_dict()]
print(dir(df.iloc[2][3]))