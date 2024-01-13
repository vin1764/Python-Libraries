import pandas as pd

movies=pd.read_csv('http://bit.ly/imdbratings')
print(movies.head())
print('\n')

#To get information about a particular column
print(movies.genre.describe())
print('\n')

#To get indepth analysis of a column:
print(movies.genre.value_counts())
print('\n')

#To get the same data in percentage form:
print(movies.genre.value_counts(normalize=True))
print('\n')

#We can also round it off to 3 digits after decimal and then multiply by 100 to get better data
print(movies.genre.value_counts(normalize=True).round(3)*100)
print('\n')

#To know what all unique values exist in a column/series
print(movies.genre.unique())
print('\n')

#To get the data between values of 2 columns:
print(pd.crosstab(movies.genre,movies.star_rating))
print('\n')
print(pd.crosstab(movies.genre,movies.content_rating))
print('\n')
print(pd.crosstab(movies.genre,movies.duration))
print('\n')

