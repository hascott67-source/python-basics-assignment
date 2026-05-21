# Simple Calculator.py
# A simple calculator that performs basic arithmetic operations

# Ask for numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Validate numeric input (simple version)
if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
    print("Error: Please enter valid numbers.")
else:
    num1 = float(num1)
    num2 = float(num2)

    # Ask for operation
    operation = input("Choose an operation (+, -, *, /): ")

    # Perform calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            exit()
        result = num1 / num2
    else:
        print("Error: Unsupported operation.")
        exit()

    # Print result
    print(f"{num1} {operation} {num2} = {result}")