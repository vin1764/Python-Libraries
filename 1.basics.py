def hello_func():
    pass          # the pass command allows us to continue without adding
                  #anything in the parameters yet

print(hello_func()) #this will print none because currently our function is empty 

def hello_func1():
    print("Hello Function")

hello_func1()    #calling a function

def hello_func2():
    return 'Hello Function'

hello_func2()     #this wouldn't print anything because the function has a string return 
print(hello_func2())#this would print whatever the function returns

#We can treat our function same as we would treat its return value. Eg:

print(hello_func2().upper())#this will print the string in the return value of the function
                            #in upper case


def greetingFunc(greeting):
    return '{} Vinayak'.format(greeting)  #we can use this to customize our function to return 
                                          #according to whatever's given as the parameter

print(greetingFunc('Goodmorning')) 

def greetFunc2(greeting='Hello',name='Vinayak'): #this can be done to pass default values for our    
    return '{},{}'.format(greeting,name)         #parameters. If the user doesn;t input any values
                                                 #the function would return with the default values


print(greetFunc2())
print(greetFunc2('Goodmorning','Isha'))




    



