import pandas as pd

drinks=pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks.head())
print('\n')

print(drinks.index)  #prints the info about indexing of the data
print('\n')

print(drinks.loc[23,'beer_servings']) #prints the value in row 23 of the 
print('\n')                           #column beer servings

#But this isn't the most useful thing since we can't always remember what
#index our data is at. Instead of this,we can set our index as some meaningful
#data,like some column from the table which has a unique value for every row

#To set one of the columns as the index column:

drinks.set_index('country',inplace=True)
print(drinks.head())
print('\n')
print(drinks.index)
print('\n')

print(drinks.shape) #The number of columns has now become 55 instead of 6 
print('\n')         #since one column has been converted to the index column

#Now, instead of searching some data with the index,we can check it by the 
#country name. Eg:
print(drinks.loc['Brazil','beer_servings'])
print('\n')

#we can remove the name of the index column by:
drinks.index.name=None
print(drinks.head())
print('\n')

#Also,we can reset back to original numbered indexing:
drinks.reset_index(inplace=True)
print(drinks.head())
print('\n')

#Here, you can see that the name of the countries column got changed to index.
#This was because we removed the column name of countries column when it was our
#index,and then we shifted it back to a column without a name. To change this:

drinks.rename(columns={'index':'country'},inplace=True)
print(drinks.head())
print('\n')
#OR
drinks.rename({'country':'Country'},axis=1,inplace=True)
print(drinks.head())
print('\n')

#Now lets say we create another dataset representing populations of countries

people=pd.Series([30000,50000],index=['Albania','Andorra'],name='Population')
print(people)
print('\n')

#Now, we can use this data to get the total beer consumption of a country by multiplying
#its population with its beer servings data.

drinks.set_index('Country',inplace=True)
print((drinks.beer_servings*people).head())
print('\n')

#Here,we can see that pandas multiplied the andorra population with andorra beer servings
#and albania populationn with albania beer servings,instead of just multiplying the first
#2 rows of the 2 datasets. This is because both the datasets have a common type of indexing,
#so pandas matched the indexing and did the multiplication according to the indexes

#Also, we can add the people data set as a series in the drinks dataset, and this will also be 
#done automatically according to the indexes.Eg:

drinks=pd.concat([drinks,people],axis=1)
print(drinks.head())
print('\n')

ufo=pd.read_csv('http://bit.ly/uforeports')
print(ufo.head())
print('\n')

#.loc COMMAND

#loc is for selecting rows/columns via their labels (labels for rows are their indexes,and
# labels for columns are their column names). Syntax of .loc is .loc(row label, column label)

print(ufo.loc[0,:])  #this will print the zeroth row and all its columns
print('\n')

print(ufo.loc[0:2,:]) #prints the 0,1,2 rows and all its columns
print('\n')

#NOTE that here x:y is inclusive of y

#.iloc COMMAND

#iloc is for selecting rows/columns via integer indexing
print(ufo.iloc[:,0:3]) # this will print all rows and columns 0,1,2 (not 3)
print('\n')


#NOTE that here x:y is exclusive of y
