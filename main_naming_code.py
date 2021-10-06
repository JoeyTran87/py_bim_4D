from os import truncate
from typing import List
import pandas as pd

pd.set_option('display.max_colwidth', 80)

def abserviation():
    file_path_abserv = r"F:\_NGHIEN CUU\_Github\py_bim_4D\XLSX\ABREVIATION.xlsx"

    excel_file_abserv = pd.ExcelFile(file_path_abserv)
    # [print(shn) for shn in excel_file_abserv.sheet_names]
    

    sheet_name = 'ABSERVIATION'

    df_abserv = pd.read_excel(excel_file_abserv,sheet_name)
    # print(df_abserv)

    abserv_headers = df_abserv.columns
    # [print(hd) for hd in list(abserv_headers)]

    col_code = "CODE"
    col_code_mean = "MEAN"

    data_code = df_abserv[col_code]
    data_code_mean = df_abserv[col_code_mean]

    dic_code = {}
    for i in range(len(data_code)):
        if str(data_code[i]) != "nan":
            dic_code[str(data_code[i])] = str(data_code_mean[i])

    # [print(f"{d} : {dic_code[d]}") for d in dic_code]
    return dic_code
