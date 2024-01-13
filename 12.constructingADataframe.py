import pandas as pd

data=pd.DataFrame({'id':['100','101','102'],'color':['red','blue','green'],'password':['ABC','BCD','CDE']},columns=['id','color','password'],index=['i','ii','iii'])
print(data)
print('\n')

#Alternatively, 

df=pd.DataFrame([[100,'red','ABC'],[101,'blue','BCD'],[102,'green','CDE']],columns=['id','color','password'])
print(df)
print('\n')

#Converting a numpy array into a dataframe
import numpy as np

arr=np.random.rand(4,2)
print(arr)
print('\n')

df1=pd.DataFrame(arr,columns=['id1','id2'])
print(df1)
print('\n')

#Creating a random dataframe having 10 rows and 2 columns:student_id and test_score
df2=pd.DataFrame({'Student_id':np.arange(100,110,1),'test_score':np.random.randint(60,101,10)})
print(df2)
print('\n')
#The value inside arange brackets stand for (starting value,end value,step) and that in the randint bracket 
#stands for (starting value, maximum value,number of randints to be generated)

#Here we can also make an existing column as the index column of the dataframe
df2=pd.DataFrame({'Student_id':np.arange(100,110,1),'test_score':np.random.randint(60,101,10)}).set_index('Student_id')
print(df2)
print('\n')

#Also, we can create an individual series and then add it to the dataframe:
s=pd.Series(['round','square','circle'],index={'iii','i','ii'},name='Shape')
print(s)
print('\n')
pd.concat([data,s],axis=0)
print(data)
print('\n')
pd.concat([data,s],axis=1)
print(data)
print('\n')
