courses=['Math','Physics','Chemistry','PDS']
for item in courses: #here, item is a variable traversing through the list courses,and the 
    print(item)      #prints each item as it traverses the courses loop

#To print the index no. as well as the element present at the index, we can use the 
#enumerate function
for index,course in enumerate(courses):
    print(index,course)

#To start the indexing from 1 instead of 0, we can do:
for index,course in enumerate(courses, start=1):
    print(index,course)



nums=[1,2,3,4,5]

for num in nums:
    print(num)
    if num==3:
        print('Found!')
        break

for num in nums:
    if num==3:
        print('Found!')
        continue
    print(num)


#NESTED LOOPS

for num in nums:
    for letter in 'abc':
        print(num,letter)

#Ranged Loop

for i in range(10): #Last number is not included
    print(i)

#To start printing x elements from a, we can set the range (a,a+x)

for i in range(1,11):
    print(i)

name='Vinayak'

for i in name:
    print(i)

courses=['Math','PDS','Art','English','History']

for course in courses:
    print(course)
    for char in course:
        print(char)

for i,value in enumerate(courses): #enumerate function is used to traverse the value at an index 
    if i==3:                       #of a list
        print(value)

for i in range(0,len(courses),2),value in enumerate(courses):
    print(i)
    print(value)
    