a=3
b=3.14
c=2

print(type(a)) #prints the data type of a
print(type(b))
print('\n')

#BASIC ARITHMETICS
print(a+b) #prints value of a+b
print(a-b) #prints value of a-b
print(a*b) #prints value of axb
print(a/c) #prints value of a divided by c (gives the exact answer(float value also possible))
           #Eg: 6/4=1.5
print(a//c)#prints the value of a divided by c but as an int value (floor division)
           #Eg: 6//4=1
print(a**c)#prints a raised to the power c (a^c)
print(a%c) #prints the remainder of a divided by c

print(6/2*3-2+1) #follows BODMAS
print(6/(2*(3-2+1)))
print('\n')

#INCREMENT/DECREMENT OF A NUMBER
num=5

num+=1     #increase num by 1
print(num)
num-=1     #decrease num by 1
print(num)
num*=10    #multiply num by 10
print(num)
num/=10    #divide num by 10
print(num)
print('\n')

#ABSOLUTE VALUE FUNCTION
print(abs(-17))  #prints absolute value(value without sign) of -17
print('\n')

#ROUNDING OFF NUMBERS
print(round(3.75)) #rounds off the given number to the nearest integer
print(round(3.75,1))#rounds off the given number to the 1st digit after decimal
print(round(473.15,-1))#rounds off the given number to the 1st digit before decimal
print('\n')

#COMPARING NUMBERS

x=3
y=2

print(x==y)
print(x!=y)
print(x<y)
print(x<=y)
print(x>y)
print(x>=y)
print('\n')

#CASTING DATA TYPES

m='100'
n='200'
print(m+n) #prints the concatenated strings m and n
m=int(m)
n=int(n)
print(m+n) #prints the sum of int values stored in m and n