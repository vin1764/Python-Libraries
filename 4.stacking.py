import numpy as np

v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])

#vertical stacking
v3=np.vstack([v1,v2])
print('vertical stack v1,v2=\n',v3)
print('\n')

#horizontal stack
v4=np.hstack([v1,v2])
print('horizontal stack=\n',v3)
print('\n')

#checking the elements under a condition
print('elements of v1>=3:\n',v1>=3)
print('\n')

print("the elements in v2 having value >=7: ",v2[v2>=7]) 
print('\n')
