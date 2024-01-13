import pandas as pd

drinks=pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks.head())
print('\n')

#Now, to check the memory occupied by our dataframe
print(drinks.info()) #This shows a memory usage of 9.2+ kb. This means
print('\n')          #that the minimum storage space taken by the dataframe is 9.2 kb.
# This is bcz in info command, pandas only checks the no. of dataspaces and not the datatype
#stored inside them. It just assumes them to be int type since int takes up the least storage
#and gives us the data. To know the actual storage space occupied:

print(drinks.info(memory_usage='deep'))
print('\n')
#Here we can see the actual storage occupied is 30kb

#The storage in bytes is:

print(drinks.memory_usage()) #gives us the storage without considering the data types of the data
print('\n')
print(drinks.memory_usage(deep=True)) #gives storage after considering the datatypes
print('\n')
print(drinks.memory_usage(deep=True).sum)#gives the total storage space of dataframe in bytes
print('\n')

#Now, what we can do to reduce the storage space occupied by the dataframe is that we can convert
#all the object datatypes to int datatypes by providing unique integer values for each unique object 
#value. In this way, we'll still have to store a small lookup table which will tell which integer code 
#stands for which object value,but the storage will be significantly reduced since we'll have to use the
#object values just once and we can usue their coded int values throughout the dataframe.
#This can be done as follows:

#Storing the continents series as int

drinks['continent']=drinks.continent.astype('category')
print(drinks.dtypes) #prints the data types of all series in the dataframe
print('\n')

#Now to check what codes have been stored for each continent:
print(drinks.continent.cat.codes.unique())#cat stands for categorical accessor,lets us access the categories
print(drinks.continent.cat.categories.unique()) #in the continents series
print('\n')                    

#Now we can check that the total storage of continents series will be significantly reduced from
#12332 to 756

print(drinks.memory_usage(deep=True))
print('\n')


#NOTE that this method is effective only for series having repeated values and not for ones having 
#all unique object values. If all object values are unique, the storage will instead increase since
#the dataframe will have to store the unique object as well as the code for each unique object! Eg:

drinks.country=drinks.country.astype('category')
print(drinks.memory_usage(deep=True))
print('\n')

print(drinks.continent.cat.codes.unique())


df=pd.DataFrame({'ID':[100,101,102,103],'quality':['good','very good','good','excellent']})
print(df)
print('\n')

#To get a sorted according to the quality dataframe:
print(df.sort_values('quality'))
print('\n')

#Here, we can see that the data got sorted alphabetically. Now we know that good, very good and excellent
#are a logical order in which a data should be sorted. If we want to get our data sorted in a logical order:

df['quality']=df.quality.astype('category',categories=['good','very good','excellent'],ordered=True)
#Here we tell pandas that the logical ordering is good<very good<excellent. This can be checked as follows:
print(df.quality)
print('\n')

print(df.sort_values('quality'))