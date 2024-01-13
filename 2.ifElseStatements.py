if True:
    print('Conditional was True')  #This will be printed since the condition in the if statement 
                                   #is true

if False:
    print('Conditional was False') #This won't be printed since the condition in the if statement 
                                   #is false

language='C++'

#IF-ELSE STATEMENT
if language=='Python':
    print('Language is Python')
else:
    print('Language is not Python')

#IF-ELIF-ELSE STATEMENT
if language=='Python':
    print('Language is Python')
elif language=='Java':
    print('Language is Java')
else:
    print('Language is',language)


#AND-OR STATEMENTS
logged_in=False
user='Admin'

if user=='Admin' and logged_in:
    print('logged_in is True') #This will be printed only if both the conditionals in the if statement
else:                          #are true
    print('logged_in is False')


if user=='Admin' or logged_in:
    print('logged_in is True') #This will be printed if atleast one of the conditionals in the if 
else:                          #statement is true
    print('logged_in is False')


if not logged_in:
    print('logged_in is False')


# 'is' CONDITIONAL

a=[1,2,3]
b=[1,2,3]
c=a

print(a==b) #This will print true since a and b are equal
print(a is b) # This will print false since a and b are equal but are different entities
print(a is c) #This will print true since a and c are same, since c changes as a changes
print( c is a)#This will print true since a and c are same, since a changes as c changes

#Values in python that evaluate to false

condition=False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition=None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition=0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition=''
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition=()
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition=[]
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition={}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#Anything other than these acts as a True condition


