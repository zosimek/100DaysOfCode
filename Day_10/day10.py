######################## IMPORTS ################################
import os

######################## STATICS ################################

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

######################## FUNCTION ###########################

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("You cannot divide by zero.")
    return a / b

def square(a, b):
    return a**b

def square_root(a, b):
    return a**(1/b)


operations = {
    "+":    add,
    "-":    subtract,
    "*":    multiply,
    "/":    divide,
    "**":   square,
    "sqrt": square_root
}

def calculations(operations, result = None, continue_calculation = True):
    while continue_calculation:
        if result == None:
            number1 = int(input("What's the first number?: "))
            result = number1
            print("+\n-\n*\n/\n**\nsqrt")
        number_initial = result
        operation = input("Pick an operation: ")
        
        while operation not in operations:
            print("Invalid operation. Please choose +, -, *, /, **, or sqrt.")
            operation = input("Pick an operation: ").strip()
            
        number_next = int(input("What's the next number?: "))
        result = operations[operation](result, number_next)
        if operation == "sqrt":
            operation = "**(1/" + str(number_next) + ")"
            print(str(number_initial) + operation + "=" + str(result))
        else:
            print(str(number_initial) + operation + str(number_next) + "=" + str(result))
        answer = input(f"""Type "y" to continue calculating with {str(result)}, or type "n" to start a new calculation: """) 
        continue_calculation = False if answer == "n" else True

########################## MAIN #############################
calculations(operations)
