courses=['Math','Physics','Chemistry','PDS']

print(courses.index('Physics')) #prints the index of the element Physics in the list1

print('Art'in courses) #prints true or false depending on whether Art is present in list1 or not
print('Math'in courses)
print('\n')

#CONVERTING LIST TO STRING
#To get the elements of a list as a comma/hyphen/space/underscore etc separated string we can use
#the join function
course_string=', '.join(courses)
print(course_string)
print('\n')
course_string1='-'.join(courses)
print(course_string1)
print('\n')

#CONVERTING STRING TO LIST
list1=course_string.split(', ')
print(list1)
print('\n')

list2=course_string1.split('-')
print(list2)
print('\n')

list3=course_string.split('-')#if we split the string at some element that isn't present in the 
print(list3)                  #string, it puts the whole string as a single element of the list
