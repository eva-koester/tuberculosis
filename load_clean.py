import pandas as pd
df = pd.read_csv('tb.csv')
print(df.head())
print(df.columns)
print(df.info())
#print(df)

# melt the df so that all gender-age columns are one column
df = pd.melt(df, id_vars=['country', 'year'], var_name='gender-age', value_name='value')
print(df.columns)

# assert that (initial col-number - id_var_no) * rows = length of rows afterwards

#print(df)


#import xlrd
#file = 'tb'
#xl = pd.ExcelFile('tb.xlsx')
#print(xl.sheet_names)