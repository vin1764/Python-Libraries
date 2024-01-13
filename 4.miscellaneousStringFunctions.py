message='Hello World'
print(message)

#To convert the string into all UPPER CASE, we use:

print(message.upper())

#Similarly, for all LOWER CASE, we use

print(message.lower())\

#To COUNT the number of occurences of a certain element or word in a string, we use:

print(message.count('Hello'))
print(message.count('l'))
print(message.count('o'))
print(message.count('H'))
print(message.count('a'))
print(message.count('h'))

#To FIND the position(index) of a certain element or a word in the string, we use

print(message.find('e'))
print(message.find('Hello'))
print(message.find('World'))
print(message.find('l')) #incase of a repeated element, it gives the position when it occurs first
print(message.find('or')) #also gives the position of a slice present in the string
print(message.find('Universe')) #incase of something not present in the string, it returns -1

#To REPLACE an element or a word in the string,

message.replace('W','G')
print(message) # This will still print Hello World because replace function didn't change the
               #message string, it made a new string with W replaced by G. To access that string
               #we need to give it a name. Eg:
new_message=message.replace('W','G')
print(new_message)
               #If we want to replace something in the same string instead of creating a new one,
               # we can just name the new string the same as our old string.
message=message.replace('W','S')
print(message)
               #Another method of doing this is by directly replacing the string inside the
               #print command.But this will just change the string for that print command only,
               #the normal string will remain the same
print(message.replace('Sorld','Universe'))
print(message)

               #if we enter something to be replaced that isn't there in
               #the string, the print command will just print the original string
print(message.replace('Universe','World'))
message=message.replace('Universe','World')
print(message)