import numpy as np

#initializing the array with all zeroes/ones
a=np.zeros((2,3))
b=np.ones((4,5))
print('a=',a)
print('b=',b)
print("\n")

#initialising with any other number
c=np.full((2,2,3),99)
print("c=",c)
print("\n")

#initialising with random numbers
d=np.random.rand(4,2)
print('d=',d)
print("\n")

e=np.random.randint(7,17,(4)) #(startvalue,endvalue,size)
print('e=',e)
print("\n") 

#printing identity matrix
f=np.identity(5)
print('f=',f)
print("\n")

#printing [1,1,1,1,1]
#         [1,0,0,0,1]
#         [1,0,9,0,1]
#         [1,0,0,0,1]
#         [1,1,1,1,1]

m=np.ones((5,5))
z=np.zeros((3,3))
z[1,1]=9
m[1:4,1:4]=z
print('m=\n',m)

