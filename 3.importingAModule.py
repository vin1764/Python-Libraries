import my_module   #import command can be used to import any file present in the same folder.If the 
                   #file is in a different folder/directory, it cannot be imported and the 
                   #import command will throw an error

courses=['History','Math','PDS','Art']

index=my_module.find_index(courses,'PDS')
print('The index of PDS in courses is ',index,'\n')

#we can also import a file and use it throughout the code using a different name for our ease
# by renaming it while importing.Eg:

import my_module2 as mm2

index1=mm2.find_index(courses,'Art')
print('The index of Art in courses is ',index1,'\n')

#Instead of importing the whole file, we can also just import a function from a file.

from my_module3 import find_index as find

index2=find(courses,'Physics')
print('The index of Physics in courses is ',index2,'\n')

#NOTE: dir() function can be used to get a list of all functions available in a module/library

print(dir(my_module)) #the functions written inside '....' are user created usable functions