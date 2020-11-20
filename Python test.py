import pandas
df=pandas.read_excel(r'c:\users\ta0094\desktop\test.xlsx')
print(df)
gb=df.groupby('Name').agg('sum')
print(gb)