import math

# Function to perform basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Function to perform scientific operations
def sqrt(x):
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number"
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

while True:
    # Display the calculator menu
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'sqrt' for square root")
    print("Enter 'power' for exponentiation")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide", "sqrt", "power"):
        num1 = float(input("Enter the first number: "))

        if user_input in ("sqrt", "power"):
            result = 0
        else:
            num2 = float(input("Enter the second number: "))

        if user_input == "add":
            result = add(num1, num2)
        elif user_input == "subtract":
            result = subtract(num1, num2)
        elif user_input == "multiply":
            result = multiply(num1, num2)
        elif user_input == "divide":
            result = divide(num1, num2)
        elif user_input == "sqrt":
            result = sqrt(num1)
        elif user_input == "power":
            exponent = float(input("Enter the exponent: "))
            result = power(num1, exponent)

        print("Result:", result)
    else:
        print("Invalid input. Please try again.")
