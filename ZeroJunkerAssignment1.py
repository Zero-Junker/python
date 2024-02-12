# INF360 - Programming in Python
# Zero Junker
# Assignment 1

#variables
myInput = 0
name = ''
y = 0
result = 0

#print messages and recive input
print('Hello! What is your name? \n')
name = input("> ")
print('Hello ' + str(name) + ', Please enter an integer')
myInput = input("> ")
print('You entered the number: ' + myInput + '\n')
print('Please enter another integer \n')
y = input("> ")
print('You entered the number: ' + y + '\n')

#Do simple math with myInput and y

#exponent
int(result)
result = int(myInput) ** int(y)
print(str(myInput) + ' to raised to the ' + str(y) + ' power is: ' + str(result) + '\n')

#modulus
int(result)
result = 0
result = int(myInput) % int(y)
print(str(myInput) + ' modulus ' + str(y) + ' is: ' + str(result) + '\n')

#integer division
int(result)
result = 0
result = int(myInput) // int(y)
print(str(myInput) + ' divided by ' + str(y) + ' with a floored quotient is: ' + str(result) + '\n')

#normal division
int(result)
result = 0
result = int(myInput)/int(y)
print(str(myInput) + ' divided by ' + str(y) + ' is: ' + str(result) + '\n')

#multiplication
int(result)
result = 0
result = int(myInput)*int(y)
print(str(myInput) + ' multyplied by ' + str(y) + ' is: ' + str(result) + '\n')

#addition
int(result)
result = 0
result = int(myInput)+int(y)
print(str(myInput) + ' added to ' + str(y) + ' is: ' + str(result) + '\n')

#subtraction
int(result)
result = 0
result = int(myInput)-int(y)
print(str(myInput) + ' subtracted from ' + str(y) + ' is: ' + str(result) + '\n')

#Ending message
print('Thank you ' + name + ', have a nice day!')
