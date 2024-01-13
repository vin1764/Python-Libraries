import pandas as pd

a=pd.read_table('http://bit.ly/chiporders') #using read_table command,pandas can read data from external
print(a)                                    #sources like excel,url,text file etc. 
print('\n')

#read_table command by default assumes the data to be tab separated,so it sorts it into columns
#accordingly.If the data isn't tab separated,we can specify the separator during our command.Also,
#it assumes the first row to be the header row by default.

print(a.head()) #this prints the first 5 rows of our data
print('\n')


b=pd.read_table('http://bit.ly/movieusers')
print(b)       #as we can see,this command did not separate the data and put it all into one column.
print('\n')    #this is because the data is not tab separated,it is separated by '|'.So,we need to 
               #specofy to our read_table command to separate the data according to the '|' separator.

c=pd.read_table('http://bit.ly/movieusers',sep='|')
print(c)            #now the data is printed after being sorted into different columns according to '|'
print('\n')

#another problem we can see in this table is that the first row is taken to be the header row by default,
#even though it isn't. We can change this as follows:

d=pd.read_table('http://bit.ly/movieusers',sep='|',header=None)
print(d)
print('\n')

#Here,we can see that in absence of a header row, it got default values as 0,1,2,3,4 integers. We can change 
#this by pre-defining the column names.Eg:

column_names=['user_id','Age','Gender','Occupation','zip_code'] #we made a list with the required column names
e=pd.read_table('http://bit.ly/movieusers',sep='|',header=None,names=column_names)
print(e)
print('\n')




