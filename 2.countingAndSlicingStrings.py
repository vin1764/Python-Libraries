#To count the number of elements/characters present in a string, we use the len function

message="Hello World"
print(len(message))

#To print a specific element of a string, we use:

print(message[0])
print(message[5])
print(message[10])

#To print a specific part of a string, we slice the string from the beginning to the end of the part required
#eg:

print(message[0:4])
print(message[4:7])
print(message[7:10])
print(message[7:11])

#Here, note that the slice includes the starting element but doesn't include the ending element

#Also note that in the last printing message, we gave the command to print from 7:11, even
#though 11th element of the string doesn't exist. This is because while printing a slice
#the last element isn't included and giving the command to print till 11 meams the slice 
#will print till the last element of the string.

#Another way of printing till the last element of the string is by leaving the end element empty
#eg:

print(message[7:])