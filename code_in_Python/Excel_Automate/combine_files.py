import numpy as np
import pandas as pd
import openpyxl
import os

folder_location = ("D:\\Users\\OneDrive\\Documents\\Work\\Syngenta\\MBR Data\\MBR Offline_Regional\\21-07-2021")
file_name = []
print(os.listdir(folder_location))

for i in os.listdir(folder_location):
    if i.endswith('.xlsx'):
        file = folder_location + "\\" + i
        print(file)
        wb = openpyxl.load_workbook(file)
        sheets = wb.sheetnames
        #print(sheets)
        for j in sheets:
            if j.__contains__("Exec"):
                print(j)
                df_exec_summ = pd.read_excel(file, sheet_name=j)

print(df_exec_summ.head())
print(df_exec_summ.describe())