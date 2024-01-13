message='Hello World'
print(message)


#if our string has single quotes in it( eg: girl's), the compiler will face error in recognising
#that which quote does the string end on...

#To avoid this, we can either use a backslash before the string's single quote
#eg:

message1='Vinayak\'s World'
print(message1)

#or we can use double quotes instread of single quote for our string
#eg:

message2="Vinayak's Universe"
print(message2)

#similarly, if the string has double quotes used in it we can use single quotes for the string
#eg:

message3='Vinayak lives in a city called "Delhi"'
print(message3)

#Another method to avoid this is using 3 quotes("""......."""). This will be useful in a general
#case when we dont know what's present in our string. So, using triple quotes will avoid both
#the single as well as the double quotes present in the string.

#eg:

message4="""Vinayak's city is called "Delhi" """
print(message4)


