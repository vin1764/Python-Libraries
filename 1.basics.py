import numpy as np

a=np.array([1,2,3,4])
print(a,'\n')

b=np.array([[1,2,3,],[4,5,6,]])
print(b,'\n')

#checking dimension of arrays
print("dimension of a =",a.ndim)
print("dimension of b =",b.ndim)
print('\n')

#checking the shape of arrays(no. of rows,columns)
print("the shape of a=",a.shape)
print("the shape of b=",b.shape)
print("\n")

#checking the memory used by and the data type of our array
print("the data type of a=",a.dtype)
print("the data type of b=",b.dtype)
print("\n")

#checking the length of array
print("size of a=",a.size)
print("size of b=",b.size)
print("\n")

#getting a specific element
print('3rd element of a=',a[2])
print('element at [0,2] in b=',b[0][2])
print("\n")

#getting a specific element using negative indexing
print('3rd element of a=',a[-2])
print('element at [0,2] in b=',b[-2][-1])
print("\n")

#printing a specific row/column
print("first row of b=",b[0])
print('3rd column of b=',b[:,2])
print("\n")

#printing specific patterns of an array(startindex:endindex:stepsize)
print(b[0,0:3:2])
print("\n")

#changing specific values
a[2]=7
print('changed a[2] to 7:',a)
b[1][2]=10
print('changed b[1][2] to 10:',b)
b[:,1]=[11,12]
print('changed the second column of b to [11,12]:',b)
print("\n")