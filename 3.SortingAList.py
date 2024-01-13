list1=['banana','abcde','alphabet','xylophone','giraffe']
print(list1)

list1.reverse() #this reverses the list
print(list1)

list1.sort() #this sorts the list(alphabetically incase of strings,ascending order incase of numbers)
print(list1)

list2=[17,5,3,8,65]
print(list2)

list2.sort()
print(list2)

list1.sort(reverse=True)#this sorts the list in descending order
list2.sort(reverse=True)
print(list1)
print(list2)

#Incase we want a sorted version of our list without altering the original list,we can do 
#this by using the sorted function.Eg:

list3=[56,32,46,89,12]
sorted_list3=sorted(list3) #this puts the sorted list3 in sorted_list3 list,keeping list3 in place
print(list3)
print(sorted_list3)


print(min(list3)) #prints the minimum element of list3
print(max(list3)) #prints the maximum element of list3
print(sum(list3)) #prints the sum of all elements of list3
