set1={'a','b','c','d'}
print(set1)

#sets are used mainly to remove duplicate elements and see only what all different elements
# are present in a list. They can also be used to check what all similar elements are 
#present between 2 different lists

#Note that on printing a set it always gives a different output,with the order
#of the elements being changed every time. This is because sets are only used to 
#represent what all elements are there in a list, independent of their order.

set2={'a','b','c','a','d','c','e'}
print(set2) #Note that printing set2 only prints all the unique elements of the set2, 
            #irrespective of their number of occuerences.

course1={'math','english','pds','chemistry'}
course2={'english','physics','mechanics','pds'}

print(course1.intersection(course2)) #This will print the common elements of the sets
print('\n')                          #course1 and course2


print(course1.union(course2))        #This will print all the courses present in the sets
print('\n')                          #course1 and course2

                                     
print(course1.difference(course2))   #This will print the courses present in set course1 but
print('\n')                          #not in course2
print(course2.difference(course1))   #This will print the courses present in set course2 but
print('\n')                          #not in course1