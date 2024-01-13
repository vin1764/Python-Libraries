import pandas as pd

movies=pd.read_csv('http://bit.ly/imdbratings')
print(movies.head())
print('\n')

#To sort according to the alphabetical order of the titles of the movies(sorts in 
# ascending order by default)

print(movies.title.sort_values())
print('\n')

#to sort in descending:
print(movies.title.sort_values(ascending=False))
print('\n')

#note that by using this method,we can only access the sorted title column of
#the dataframe. In order to access the whole dataframe sorted according to the title:

print(movies.sort_values('title'))
print('\n')

#to pass a dataframe according to more than one columns:

print(movies.sort_values(['content_rating','duration'])) #Note that this method is going to follow the priority order 
print('\n')     #in which the columns are written,i.e. it will first sort the data according to the content_rating and
#then further according to the duration

#Sometimes we need to sort our data according to a particular value. For this one,let's say we need the list and details 
#of all movies that are longer than 200 mins.This can be done as follows:

#1)Long method:

bool=[]
for length in movies.duration:   #we create a new list which is as long as our movies list and contains True value at
    if length>=200:              #all those indexes in which our movie duration is >=200 in the movies.duration column
        bool.append(True)
    else:
        bool.append(False)

long_movies=pd.Series(bool)      #we convert the bool list into a single column of a dataframe

print(movies[long_movies])  #this command prints the list of movies which have a true value in the long_movies column
print('\n')

#2) Shortcut
print(movies[movies.duration>=200])
print('\n')

#Using multiple conditions to filter the dataframe:
print(movies[(movies.duration>=200)&(movies.genre=='Drama')])
print('\n')

print(movies[(movies.star_rating>=9)|(movies.genre=='Crime')])
print('\n')

#For multiple or conditions under a single column, we can use the isin command. Eg:
print(movies[(movies.genre=='Crime')|(movies.genre=='Action')|(movies.genre=='Drama')])
print('\n')
#instead of doing this, we can do:
print(movies[movies.genre.isin(['Crime','Action','Drama'])])
print('\n')