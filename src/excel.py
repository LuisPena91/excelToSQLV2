import pandas as pd
from menu import menu2
from pathlib import Path

#Func to read the excel book
def read_excel(file_path, sheet_name):
    return pd.read_excel(file_path,sheet_name=sheet_name)
#func to list the sheets in the excel book
def sheet_names_excel(excel_file_path):
    excel_file = pd.ExcelFile(excel_file_path)
    sheet_names = excel_file.sheet_names
    return sheet_names
#func to select a sheet
def sheet_number(excel_file_path):
    print('----> Excel Tables <----')
    for i in range(len(sheet_names_excel(excel_file_path))):
        print(f" - {i+1}:  {sheet_names_excel(excel_file_path)[i]}")
    print(" - 0:  Return")
    sheet_excel = menu2(i+1)
    return sheet_excel-1
#fun to select a column from the sheet
def column_number(columns):
    print('----Excel Columns----')
    for i in range(len(columns)):
        print(f" - {i+1}:  {columns[i]}")
    print(" - 0:  Start over")
    column = menu2(i+1)
    return column-1
#fun to control the null values
def df_null_values(df):
    for c in df.columns:
        if df[c].dtype == 'object': #to strings
            df[c] = df[c].fillna('NA')
        elif pd.api.types.is_numeric_dtype(df[c]): #to numbers
            df[c] = df[c].fillna(0)
        elif pd.api.types.is_datetime64_any_dtype(df[c]): #to dates
            df[c] = df[c].fillna(pd.Timestamp('1900-01-01'))
        elif pd.api.types.is_timedelta64_dtype(df[c]): #to time delta
            df[c] = df[c].fillna(pd.Timedelta('0 days'))
        elif pd.api.types.is_time_dtype(df[c]): #to time
            df[c] = df[c].fillna(pd.Timestamp('00:00:00').time())
    return df
#Func to check if the excel file exist
def file_check(file):
    while True:
        try:
            with open(file, 'r'):
                return file
        except FileNotFoundError:
            print("File was not founded.")
            file = input("Copy a valid document path: ")
        except IOError:
            print("There is a error trying to open the file")
            file = input("Copy a valid document path: ")
