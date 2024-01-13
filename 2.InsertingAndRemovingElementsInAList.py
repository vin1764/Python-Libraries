courses= ['Math','Physics','Chemistry','PDS']

courses.append('Art') #This will add 'Art' as a new element at the last in the list courses
print(courses)
print('\n')

courses.insert(2,'Robotics')#This will insert 'Robotics as a new element in the list at the 2nd index
print(courses)
print('\n')

#LIST WITHIN A LIST
courses1= ['Math','Physics','Chemistry','PDS']
courses2=['History','Geography']
courses1.insert(0,courses2)#This will add the whole list courses2 as an element in the list courses1
print(courses1)            #at the index 0
print(courses1[0]) #this will print the whole index 0 of courses1 i.e. the courses2 list
print('\n')

#But, if we want to add the elements of the list courses 2 into the list courses1 as individual 
#elements in the list courses, we can use the extend function

courses.extend(courses2)
print(courses)
print('\n')

#Note that if we create a list x and equate it to an existing list y,then any changed made to x will
#be applied to y and vice versa

x=['a','b','c']
print(x)
y=x
print(y)
y.insert(1,'d')
print(y)
print(x)
x.insert(3,'e')
print(x)
print(y)
print('\n')

#REMOVING ELEMENTS FROM A LIST
m=['p','q','r','s','t']
print(m)
m.remove('r') #removes the element r from the list m
print(m)
m.pop() #removes the last element from the list m
print(m)
print('\n')

#Note that the pop function actually returns the popped element. Eg:
popped_element=m.pop()
print(popped_element)
print(m)
