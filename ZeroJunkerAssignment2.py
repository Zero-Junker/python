# INF360 - Programming in Python
# Zero Junker
# Assignment 2

import random

#variables
randomInt1 = 0
randomInt2 = 0
choice = 0
result = 0


#start of while statment


while choice != 4:
    print("please select a function: ")
    print("1. Multiply two random numbers")
    print("2. Get the factorial of a random number")
    print("3. find the larger number between two random numbers")
    print("4. Exit program")
    choice = input("> ")
    if choice == '1':
        #get two random ints
        int(randomInt1)
        randomInt1 = random.randint(1,100)
        int(randomInt2)
        randomInt2 = random.randint(1,100)
        int(result)
        result = randomInt1 * randomInt2
        print("The product of " + str(randomInt1) + " and " + str(randomInt2) + " is: " + str(result))
        continue
    elif choice == '2':
        #get the factorial of a random number
        int(randomInt1)
        randomInt1 = random.randint(1,10)
        int(result)
        result = 1
        for x in range(1,randomInt1 + 1):
            result = result * x
        print("The factoral of " + str(randomInt1) + " is: " + str(result))
        continue
    elif choice == '3':
        #find the larger of two random numbers
        int(randomInt1)
        randomInt1 = random.randint(1,100)
        int(randomInt2)
        randomInt2 = random.randint(1,100)
        if randomInt1 > randomInt2:
            print( str(randomInt1) + " is larger than " + str(randomInt2))
        elif randomInt1 < randomInt2:
            print( str(randomInt1) + " is smaller than " + str(randomInt2))
        else:
            print( str(randomInt1) + " is equal to " + str(randomInt2))
    elif choice == '4':
        print("Have a nice day!")
        break;
    else: #if the number entered is not 1,2,3, or 4 have the user enter a different number
        print("Invalid selection please enter a number between 1 and 4")
        choice = input("> ")
