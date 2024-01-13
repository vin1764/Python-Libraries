#Equating 2 variables
#When we simply equate 2 variables, we don't create a new object, we just creates a new variable 
#referencing the same object. This means that any changes done in the original variable will
#reflect in the new variable and vice-versa.

a=[1,2,3]
b=a
print(b)
print(id(a))
print(id(b)) #both a and b have the same address

a.append(4)
print(a) 
print(b) #change observed

b.append(5)
print(b)
print(a) #change observed

a[1]=9
print(a)
print(b) #change observed

b[1]=10
print(b)
print(a) #change observed


import copy

#SHALLOW COPY

#In this, we don't observe changes in the copy if there are any changes in the original list. But, 
#if changes are done in a nested list of the original list, changes will be reflected in the nested
#list of the copy as well.
x=[6,[7,8,9],10]
shallow_copy=copy.copy(x)
print(x)
print(shallow_copy)
print(id(x))
print(id(shallow_copy)) #list x and shallow copy of x have different address
print(id(x[1]))
print(id(shallow_copy[1])) #but nested list of x and its shallow copy have the same address

x.append(11)
print(x)
print(shallow_copy) #no change observed

x[0]=5
print(x)
print(shallow_copy) #no change observed

x[1][1]=11
print(x)
print(shallow_copy) #change observed

#DEEP COPY

#In this, the copy formed is a completely independent copy which reflects no changes,
#whatever may be done in the original list

p=[3,[4,5,6],7]
deep_copy=copy.deepcopy(p)
print(p)
print(deep_copy)
print(id(p))
print(id(deep_copy)) #list p and deep copy of p have different address
print(id(p[1]))
print(id(deep_copy[1])) #as well as the nested list of p and its deep copy have different address



p.append(8)
print(p)
print(deep_copy) #no change observed

p[0]=1
print(p)
print(deep_copy) #no change observed

p[1][1]=9
print(p)
print(deep_copy) #no change observed



