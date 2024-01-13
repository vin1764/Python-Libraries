import pandas as pd

drinks=pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks)
print('\n')
#Here, we can see that only the first and the last few rows are visible to us
print(pd.get_option('display.max_rows'))#To check how many rows are visible by default
print('\n')

#Now, if we want to see all the rows:
pd.set_option('display.max_rows',None)
print(drinks)
print('\n')

train=pd.read_csv('http://bit.ly/kaggletrain')
print(train.head())
print('\n')

#Here, we can see that in the first row in the Name column..there is a ... after the name.
#This is because the name might be long and it exceeds the default display settings allowed
#in a column width. To see how much characters are allowed by default:
print(pd.get_option('display.max_colwidth'))
print('\n')

#Here, the default col width is 50. To change it to lets say 1000
pd.set_option('display.max_colwidth',1000)
print(train.head())
print('\n')

#Also, in the fare column, we can see fare upto 4 decimal places. Lets say we want it upto 
#a precision of 2 decimal places:
pd.set_option('display.precision',2)
print(train.Fare.head())
print('\n')

#Sometimes, we have large numbers and we want them to be comma separated. Lets first create a 
#column having large numbers in the database

train['x']=train.Fare*10000
print(train.x.head())
#To convert it into it comma separated digits:

pd.set_option('display.float_format','{:,}'.format) #This tells pandas to use comma as the separator
print(train.x.head()) #If we write '{:_}', the digits will be separated by _ instead of a comma

#NOTE that this only affects columns that have a float value. If the large numbers are int they would
#remain the same since there is no int_format option
