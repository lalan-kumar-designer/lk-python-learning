# Exception Handling

# Handle an error using try and except.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter valid numbers.")


# Use else when no exception occurs.
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("Number:", number)


# Use finally to execute code whether an error occurs or not.
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
finally:
    print("Program completed.")