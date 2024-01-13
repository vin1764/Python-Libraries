#A list stands for a group of sequential data
#Eg: creating a list of courses

courses= ['Math','Physics','Chemistry','PDS'] #this will create a list named courses having 4 
                                              #elements, math,physics,chemistry and pds

print(courses) #this will print all the elements of the list 'courses'
print('\n')

print(len(courses)) #this will print the number of elements in the list courses

print(courses[0]) #prints the element present at 0th index in the list
print(courses[1]) #prints the element present at 1st index in the list
print(courses[2]) #prints the element present at 2nd index in the list
print(courses[3]) #prints the element present at 3rd index in the list
print(courses[-1])#prints the element present at the last index in the list
print(courses[-2])#prints the element present at the second last index in the list
print('\n')

print(courses[0:2])#prints the elements from the 0th index to the 2nd index(0th included,2nd not included)
print(courses[2:4])#prints the elements from the 2nd to the 4th index(note that since 4th index is not included,
                   #the compiler does not show an error in printing from 2nd to 4th index since this means it will
                   #print the 2nd and 3rd index elements only!)
print(courses[:3]) #prints the elements from the starting to the 3rd index(3rd not included)
print(courses[1:]) #prints the elements from the 1st element to the last element