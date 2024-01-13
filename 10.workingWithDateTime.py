import pandas as pd

ufo=pd.read_csv('http://bit.ly/uforeports')
print(ufo.head())
print('\n')

#here, we can convert the time series's datatype from object to datetime

ufo.Time=pd.to_datetime(ufo.Time)
print(ufo.head())
print('\n')

#To get specific details about the datetime of the data:
print(ufo.Time.dt.year.head())
print('\n')
print(ufo.Time.dt.month.head())
print('\n')
print(ufo.Time.dt.day.head())
print('\n')
print(ufo.Time.dt.weekday.head())
print('\n')
print(ufo.Time.dt.day_name().head())
print('\n')
print(ufo.Time.dt.hour.head())
print('\n')
print(ufo.Time.dt.minute.head())
print('\n')
print(ufo.Time.dt.second.head())
print('\n')
print(ufo.Time.dt.day_of_year.head())
print('\n')

#we can also use datetime commands for comparisons,by creating a sample
#timestamp

ts=pd.to_datetime('1/1/1999')

print(ufo.loc[ufo.Time>ts].head())#this will print all rows in the ufo dataframe
print('\n')#that are ahead in time than 1/1/1999

#To know the latest timestamp in the dataframe:
print(ufo.Time.max())
print('\n')

#to know how much is the time between the first and the last timestamp:
print(ufo.Time.max()-ufo.Time.min())
print('\n')
print((ufo.Time.max()-ufo.Time.min()).days)
print('\n')

