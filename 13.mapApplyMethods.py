import pandas as pd
import numpy as np

train=pd.read_csv('http://bit.ly/kaggletrain')
print(train.head())
print('\n')

#Here, lets say we want to create a series called sex_num in which we want to have 
#only zeroes and ones corresponding to the sex of the person, i.e. we want to map
#female to 0 and male to 1

train['sex_num']=train.Sex.map({'male':0,'female':1})
print(train.loc[:,['Sex','sex_num']].head())
print('\n')

#APPLY METHOD:It applies a function to each element in a series

#lets say we want to calculate the length of the string in each element of the name column,
#and then store it in a new column called name_length

train['name_length']=train.Name.apply(len)
print(train.loc[:,['Name','name_length']].head())
print('\n')

#Lets say we want the last name of each person stored in a separate column. For this, we'll
#have to separate the name at the commas. For this we can use the str.split function

print(train.Name.str.split(',').head())#This gives us a list having 2 elements,the last name
print('\n')          #and the first name, and what we want is only the first element(last name)

#For this we can define a function and then apply that function on this list

def get_element(my_list,position):
    return my_list[position]

train['last_name']=train.Name.str.split(',').apply(get_element,position=0)
print(train.last_name.head())
print('\n')

drinks=pd.read_csv('http://bit.ly/drinksbycountry')
#now let say we want the max value in each of the columns beerservings,wineservings and spiriti servings

print(drinks.loc[:,'beer_servings':'wine_servings'].apply(max,axis=0).head())
print('\n')

#similarly,we want the max value in each row across the 3 columns:
print(drinks.loc[:,'beer_servings':'wine_servings'].apply(max,axis=1).head())
print('\n')

#Also, instead of knowing what is the maximum value in each row, we instead want to know which column has the 
#maximum value for each row:

print(drinks.loc[:,'beer_servings':'wine_servings'].apply(np.argmax,axis=1).head())
print('\n')

#APPLYMAP FUNCTION

#This applies a function to all the elements of a dataframe
print(drinks.loc[:,'beer_servings':'wine_servings'].applymap(float).head())#this converts the values in all elements to a float value
print('\n')