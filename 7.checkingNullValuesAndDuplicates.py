import pandas as pd
ufo=pd.read_csv('http://bit.ly/uforeports')

print(ufo.tail)
print('\n')
#Here, the NaN values refer to values that were empty/missing in the dataframe

#To check what all rows a have a null value:
print(ufo.isnull()) #True refers to value is null,False means it has some value
print('\n')

#To check number of missing values in each column:
print(ufo.isnull().sum())
print('\n')

#To get a list of only the null values of a column:
print(ufo[ufo.City.isnull()])
print('\n') 

#To remove all the rows which have even one empty value:
print(ufo.dropna(how='any')) #how='any' refers to dropping rows that have any value empty
print('\n')                  #However,we can simply write ufo.drop(),and this will do the same 
                             #task since how='any' is the default value
                             
#Whereas if we only want to drop rows that have all values empty
print(ufo.dropna(how='all'))
print('\n')

print(ufo.dropna(subset=['City','Shape Reported'],how='any')) #this drops rows which have any values
print('\n')                                            #lying in the following subset of columns as empty

#To change an empty value to an existing/new value
ufo['Shape Reported'].fillna(value='VARIOUS',inplace=True)
print(ufo['Shape Reported'])
print('\n')

user_cols=['user_id','age','gender','occupation','zip_code']
users=pd.read_table('http://bit.ly/movieusers',sep='|',header=None,names=user_cols,index_col='user_id')
print(users.head())
print('\n')

#To check duplicates in zipcode:
print(users.zip_code.duplicated()) #This prints True if for any zipcode there exists any other same zipcode
print('\n')                        #value above it, else False

#To see if there are any same rows in the dataframe:
print(users.duplicated().sum()) #prints the number of duplicate rows in the dataframe
print('\n')

#To see which rows are duplicate:
print(users.loc[users.duplicated(),:])
print('\n')

#Bydefault, the duplicated method has keep=first , which means it will keep the first occurence of the 
# duplicated rows in the dataframe and count the rest of them as duplicates. Alternatively, we can also change 
#it to keep=last, to keep the last occurence of the repeated rows in the dataframe and count all of them
#before it as duplicates

print(users.loc[users.duplicated(keep='last'),:])
print('\n')

#We can also see all of the duplicated rows by keeping keep=False
print(users.loc[users.duplicated(keep=False),:])
print('\n')

#To remove the duplicate rows(keeping the first occurence in the datarframe by default)

users.drop_duplicates(inplace=True)
print(users.shape)
print('\n')

#To check duplicated rows only for some specific columns, i.e. lets say we need rows that have duplicated
#age and zipcode

print(users.duplicated(subset=['age', 'zip_code']).sum())
print('\n')

#we can also check for rows that have either duplicated age or duplicated zip_code
print(users.duplicated(subset=['age' or 'zip_code']).sum())
print('\n')

#Similarly,we can also use drop_duplicates method with this command to remove these duplicate rows

