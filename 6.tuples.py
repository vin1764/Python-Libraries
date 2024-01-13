#tuples are exactly like lists apart from the fact that they are immutable i.e. the elements of 
#a tuple are fixed, they can't be changed like a list.

#So, we cannot perform remove,pop,insert,append,sort etc functions on a tuple, but otherwise,
#they work the same as a list

list1=['a','b','c','d']
tuple1=('a','b','c','d')

list1.remove('c') #this will remove c from the list1
#tuple.remove('c') #this will show an error 
print(list1)
print(tuple1)