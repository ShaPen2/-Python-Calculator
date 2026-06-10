import math

def addition(input1, input2): 
    return input1 + input2

def subtraction(input1, input2):
    return input1 - input2

def multiplication(input1, input2):
    return input1 * input2

def division(input1, input2):
    return input1 / input2

def exponetial(input1, input2):
    return input1 ** input2

def square_root(smallinput):
    return math.sqrt(smallinput)

def cube_root(smallinput):
    return math.cbrt(smallinput)

def factorial(smallinput):
    return math.factorial(smallinput)

#these functions do the calculation and then return the answer


while True:
    print("")
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("5 = Exponetial")
    print("6 = Square Root")
    print("7 = Cube Root")
    print("8 = Factorial")
    print("") #all the print("") are used to make the user experience more spaced out

    #this is used to let the user pick their operation
    
    operation = int(input("What operation do you want to perform? (1, 2, 3, 4, 5, 6, 7, 8): "))

    if operation in [6,7,8]: #this filters out the operations that require only one input
        
        print("")
        smallinput = int(input("What is your input?: "))
        print("")

        if operation == 6:
            print("The square root of",smallinput, "=", square_root(smallinput))
            print("")

        if operation == 7:
            print("The cube root of",smallinput, "=", cube_root(smallinput))
            print("")

        if operation == 8:
            print(smallinput, "factorial =", factorial(smallinput))
            print("")
        
        next = input("Do you wish to do another calculation? (y/n)") #this allows the user to do a different calculation or quit
        if next.lower() == "n":
            break
        if next.lower() == "y": #the lower ensures that if the user inputs an upper case n or y it doesnt cause an error
            continue
        
    
    if operation not in [1,2,3,4,5]: #this ensures that any operations called that dont exist dont end the program
                                     # it doesnt include 6,7,8 as the code for those operations is called earlier and therfore doent need to be accounted for
        print("")
        print("invalid input")
        print("")
        
        continue
    print("")
    input1 = int(input("What is your first number?: "))
    input2 = int(input("What is your second number?: "))
    print("")
    if operation == 1:
        print(input1, "+", input2, "=", addition(input1, input2))

    elif operation == 2:
        print(input1, "-", input2, "=",subtraction(input1, input2))

    elif operation == 3:
        print(input1, "x", input2, "=", multiplication(input1, input2))

    elif operation == 4:
        print(input1, "÷", input2, "=", division(input1, input2))

    elif operation == 5:
        print(input1, "to the power of", input2, "=", exponetial(input1, input2))

    
    print("")
    next = input("Do you wish to do another calculation? (y/n)")
    if next.lower() == "n":
        break
    if next.lower() == "y":
        continue

    else:
        print("")
        print("invalid input!") #this is a fail safe so that any other invalid inputs are registered
        print("")
        continue

        








