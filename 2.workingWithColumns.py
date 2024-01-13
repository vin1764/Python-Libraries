import pandas as pd

ufo=pd.read_table('http://bit.ly/uforeports',sep=',')
#instead of this,we can also use the read_csv function,which by default assumes comma to be
#the separator

ufo=pd.read_csv('http://bit.ly/uforeports')
print(ufo[0:11]) #we can use ufo[0:x+1] command to see just the first x rows of the table ufo
print('\n')

print(ufo['City']) #prints only the City series of the table
print('\n')
#another syntax to do the same thing can be(printing only the first 10 rows):
print(ufo.City[0:11])
print('\n')

#NOTE:If the column name has a space,dot notation won't work for it! We'll have to do it normally.
#Also,we cannot use dot notation for columns that are named same as some builtin attributes. Eg:
# shape,head etc.

print(ufo['Colors Reported'][0:11])
print('\n')

#Also,if we wnt to create a new series in our dataframe, we need to use the bracket notation(the
# dot notation won't work). Eg:

ufo['Location']=ufo.City + ',' + ufo.State #a new column named Location will be created whose
print(ufo[0:11])         #contents will be the contents of city and state columns separated by a ','
print('\n')

#If you want to change the name of a particular column:
ufo.rename(columns={'Colors Reported':'color reported','Shape Reported':'Shapes REPORTED'},inplace=True)
print(ufo[0:11])
print('\n')

#Another method can be to create a list with all the new names and overwrite it on the dataframe

ufo_cols=['city','colors REPORTED','shape reported','STATE','TIME','LOCATION']
ufo.columns=ufo_cols
print(ufo[0:11])
print('\n')

#Now let's say we have a large number of columns and we only want to change the names of columns
#that have a spacxe in their names and replace the space with an _

ufo.columns=ufo.columns.str.replace(' ','_')
print(ufo[0:11])
print('\n')

#To remove a column from a dataframe
ufo.drop('colors_REPORTED',axis=1,inplace=True)
print(ufo[0:11])
print('\n')

#To remove more than one columns, add a list of strings instead of strings.
#Eg: ufo.drop(['colors reported','time'],axis=1,inplace=True)

#Also, to remove a row instead of a column, use axis=0 instead of axis=1,since axis=0 stands for rows 
#while axis=1 stands for columns
ufo.drop([0,1],axis=0,inplace=True)
print(ufo.head())
print('\n')

#here,notice that after deleting the first 2 rows,the indexing of the table
# starts from 2,3,4...To change this and start from the normal indexing:
ufo.reset_index(inplace=True)
print(ufo.head())
print('\n')