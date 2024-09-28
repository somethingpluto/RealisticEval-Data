# This demo program was created with ChatGPT.  :)
# I changed the function return values to 0, so we have
# changes to implement.

def add(a, b):
    """Function to add two numbers"""
    return 0 

def subtract(a, b):
    """Function to subtract two numbers"""
    return 0

def multiply(a, b):
    """Function to multiply two numbers"""
    return 0

def divide(a, b):
    """Function to divide two numbers"""
    return 0

print("Welcome to the Calculator!")

while True:
    print("Please select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Invalid choice. Please try again.")