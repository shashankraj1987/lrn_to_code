import pandas as pd
import os
from openpyxl import load_workbook
#import xlsxwriter
#from shutil import copyfile

file="D:/Users/shash/Documents/Learning/Python/Paypal_Incidents.xlsx"
extension = os.path.splitext(file)[1]
filename = os.path.splitext(file)[0]
pth=os.path.dirname(file)
newfile=os.path.join(pth,filename+'_2'+extension)
df=pd.read_excel(file, 'Sheet2')

size_of_df = len(df)
Col_names=("Sr.No", "Incident","SR","State","Priority","Submitted","Assigned","Closed","Efforts(Mins)","Efforts(Hrs)")

#for x in size_of_df:
 #   if df


