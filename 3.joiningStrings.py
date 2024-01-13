greeting='Hello'
name='Vinayak'

#we can join 2 or more strings together by directly using the plus sign

message=greeting+name
print(message)

#To add a space or any other word/character between the 2 strings, we can just type it in quotes 
#and add a plus sign. Eg:

message=greeting+', '+name+'. Welcome!'
print(message)

#Another way of doing this for longer strings having multiple variables is by using {}

message='{}, {}. Welcome back!'.format(greeting,name)
print(message)   #{} can be used to represent the position of variables and the variables to be
                 #entered can be directly put in order in the format parenthesis

print('{}, {}. Welcome back, again!'.format(greeting,name))  #This can also be printed by directly entering
                                                 #the required string in the print command

#Another method of joining strings is using fstrings(add an f infront of the string)

message=f'{greeting}, {name}. Welcome back!'
print(message)
#this can be used to edit the variables directly in the string. Let's say we want to capitalise
#the name :

message=f'{greeting.lower()}, {name.upper()}. Welcome!'
print(message)