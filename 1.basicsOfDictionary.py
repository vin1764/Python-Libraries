#Dicitionaries are used to store more than one type of data about a particular thing

student={'Name':'Vinayak','Age':'18','Courses':['Math','Physics']}
print(student) #This prints all data about the student

print(student['Name']) #This prints student's Name
print(student['Age']) #This prints student's Age
print(student['Courses']) #This prints student's Courses

#Sometimes, we may ask for a data that isn't present in our dictionary.This might
#throw an error. To avoid having an error,we can use the get command:

print(student.get('Phone')) #Now, using the get option, this will return None, instead
                            #of throwing off an error
#We can also specify what return do we want incase of absence of a data entry. Eg:

print(student.get('Phone','Not found')) #Now, this will return Not Found


#INSERTING DATA ENTRIES INSIDE A DICTIONARY
student['Phone']='555-6666-777'
print(student['Phone'])

#UPDATING DATA INSIDE A DICTIONARY
student['Name']='Virmani'

print(student)

#To update more than one data entry at once:
student.update({'Name':'Vinayak','Age':'19','Courses':['PDS','Chemistry']})
print(student)

#Deleting a data entry from the Dictionary
del student['Age']
print(student)

student_courses=student.pop('Courses')
print(student)
print(student_courses)

#Checking data entries inside a dictionary

print(len(student)) #prints the number of keys inside the dictionary
print(student.keys()) #prints the keys inside the dictionary
print(student.items()) #prints all the keys with their entries present in the dictionary

for key in student:
    print(key)     #this prints all the keys of the dictionary student

for key,items in student.items():
    print(key,items)  #this prints all the keys present in the dictionary along with their entries