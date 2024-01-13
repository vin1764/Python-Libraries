import pandas as pd

stocks=pd.read_csv('http://bit.ly/smallstocks')
print(stocks)
print('\n')

print(stocks.index)
print('\n')

#To check the avg closing price for each company:
print(stocks.groupby('Symbol').Close.mean())
print('\n')

#To check the closing price for each company and date:
series=stocks.groupby(['Symbol','Date']).Close.mean()
print(series)
print('\n')
#To see the index of this series:
print(series.index) # We can see that this series has a multiindex
print('\n')

#To convert this multidimensional index to a dataframe:
print(series.unstack())
print('\n')
#Another way to get the same data:
print(stocks.pivot_table(values='Close',index='Symbol',columns='Date'))
print('\n')

 