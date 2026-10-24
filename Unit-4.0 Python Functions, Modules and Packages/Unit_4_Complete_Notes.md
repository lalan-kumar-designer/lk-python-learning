# Unit 4 — Python Functions, Modules and Packages

## Functions in Python

A function is a block of code that performs a specific task. Functions help us reuse code and avoid repetition.

### Types of Functions

Python functions are divided into three types:

- Built-in Functions
- Functions Defined in a Module
- User-defined Functions

### Built-in Functions

Built-in functions are already available in Python and can be used directly.

| Function | Purpose |
|---|---|
| `print()` | Displays output |
| `len()` | Returns length |
| `max()` | Returns the largest value |
| `min()` | Returns the smallest value |
| `sum()` | Returns the sum |
| `type()` | Returns the data type |

    print("Hello World")
    print(len("Python"))
    print(max(10, 20, 30))
    print(min(10, 20, 30))
    print(sum([10, 20, 30]))
    print(type(10))

### Functions Defined in a Module

A module is a Python file containing reusable code, such as functions and variables.

    import math

    print(math.sqrt(25))
    print(math.factorial(5))

Here, `sqrt()` returns the square root and `factorial()` returns the factorial of a number.

### User-defined Functions

A user-defined function is created by the programmer using the `def` keyword.

    def greet():
        print("Hello Student")

    greet()

## Arguments and Parameters

A parameter is a variable written inside the parentheses of a function definition. An argument is the actual value passed when the function is called.

    def add(a, b):
        print(a + b)

    add(10, 20)

Here, `a` and `b` are parameters, while `10` and `20` are arguments.

## Default Parameters

A default parameter has a predefined value that is used when no argument is provided for it.

    def greet(name="Student"):
        print("Hello", name)

    greet()
    greet("Lalan")

Output:

    Hello Student
    Hello Lalan

Another example:

    def add(a, b=10):
        print(a + b)

    add(5)
    add(5, 20)

Output:

    15
    25

Parameters without default values must come before parameters with default values.

## Positional Parameters

In positional argument passing, values are assigned to parameters according to their positions in the function call.

    def student(name, age):
        print("Name:", name)
        print("Age:", age)

    student("Lalan", 17)

The order of arguments matters.

    def subtract(a, b):
        print(a - b)

    subtract(20, 5)
    subtract(5, 20)

Output:

    15
    -15

## Lambda Functions

A lambda function is a small anonymous function created using the `lambda` keyword.

Syntax:

    lambda arguments: expression

Example:

    add = lambda a, b: a + b
    print(add(10, 20))

    square = lambda x: x * x
    print(square(5))

    multiply = lambda a, b: a * b
    print(multiply(4, 5))

A lambda function can accept multiple arguments but contains only one expression.

## Returning Value

The `return` statement sends a value from a function back to the caller.

    def add(a, b):
        return a + b

    result = add(10, 20)
    print(result)

Another example:

    def square(number):
        return number * number

    print(square(5))

Example — Area of a Rectangle:

    def calculate_area(length, width):
        return length * width

    area = calculate_area(5, 4)
    print("Area:", area)

### Difference Between `print()` and `return`

- `print()` displays information on the screen.
- `return` sends a value back to the caller.
- A returned value can be stored in a variable or used in another calculation.

## Scope of a Variable

Variable scope determines where a variable can be accessed in a program.

### Local Scope

A local variable is defined inside a function and is normally accessible only within that function.

    def display():
        y = 50
        print(y)

    display()

### Global Scope

A global variable is defined outside a function.

    x = 100

    def display():
        print(x)

    display()
    print(x)

### Local and Global Variables with the Same Name

    a = 10

    def show():
        a = 20
        print("Local a:", a)

    show()
    print("Global a:", a)

Output:

    Local a: 20
    Global a: 10

The local variable does not change the global variable.

### The `global` Keyword

The `global` keyword allows a function to assign a new value to a global variable.

    number = 5

    def change():
        global number
        number = 15

    change()
    print(number)

Output:

    15

# Modules and Packages

## Modules in Python

A module is a Python file containing reusable code. The `import` keyword makes a module available in a program.

### Importing a Module

The `math` module provides mathematical functions and constants.

    import math

    print(math.sqrt(25))
    print(math.factorial(5))

### The `random` Module

The `random` module provides functions for generating random values.

    import random

    print(random.randint(1, 10))

`randint(1, 10)` returns a random integer from 1 to 10, including both limits.

### The `datetime` Module

The `datetime` module provides classes and functions for working with dates and times.

    import datetime

    print(datetime.date.today())

### Importing Specific Functions and Constants

The `from` keyword allows specific functions or constants to be imported from a module.

    from math import pi, pow

    print(pi)
    print(pow(2, 3))

### Importing a Module with an Alias

The `as` keyword gives a module a shorter name.

    import math as m

    print(m.sqrt(64))

## Regular Expressions

Regular expressions are used to search, match and replace text according to a pattern. Python provides the `re` module for this purpose.

    import re

### `search()`

Searches for a pattern anywhere in a string.

    text = "Python Programming"
    result = re.search("Python", text)

    if result:
        print(result.group())
    else:
        print("Not Found")

### `findall()`

Returns all matches of a pattern.

    text = "My marks are 75 and 85"
    print(re.findall(r"\d+", text))

Output:

    ['75', '85']

The pattern `\d+` matches one or more digits.

### `match()`

Checks for a match at the beginning of a string.

    text = "Python is easy"
    result = re.match("Python", text)

    if result:
        print(result.group())
    else:
        print("No Match")

### `sub()`

Replaces matching text.

    text = "I like Java"
    print(re.sub("Java", "Python", text))

Output:

    I like Python

### `fullmatch()`

Checks whether the entire string matches a pattern.

    text = "12345"
    result = re.fullmatch(r"\d+", text)
    print(bool(result))

Output:

    True

## Exception Handling

An exception is an error that occurs while a program is running. Python uses `try`, `except`, `else` and `finally` to handle exceptions.

### `try` and `except`

    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Please enter valid numbers.")

`ZeroDivisionError` occurs when division by zero is attempted. `ValueError` can occur when input cannot be converted to an integer.

### `else`

The `else` block runs when no exception occurs in the `try` block.

    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input.")
    else:
        print("Number:", number)

### `finally`

The `finally` block runs whether an exception occurs or not.

    try:
        print(10 / 2)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    finally:
        print("Program completed.")

## PyPI — Python Package Index

PyPI stands for Python Package Index. It is an online repository where Python packages are published and made available for installation.

Website: https://pypi.org/

## pip — Python Package Manager

`pip` is used to install and manage Python packages.

### Check the pip Version

Run this command in the terminal:

    python -m pip --version

### Install a Package

    python -m pip install requests

### Use an Installed Package

    import requests

    response = requests.get("https://example.com")
    print("Status Code:", response.status_code)

The `requests` package must be installed before it can be imported.

Commands such as `python -m pip install requests` are entered in the terminal, not directly as Python statements inside a `.py` file.

## Importing Libraries and Functions

Libraries provide reusable code for particular tasks. Python's standard library includes modules such as `math`, `random`, `datetime` and `statistics`.

### Import a Complete Module

    import math

    print(math.sqrt(36))

### Import Specific Functions

    from math import sqrt, factorial

    print(sqrt(49))
    print(factorial(5))

### Import with an Alias

    import random as r

    print(r.randint(1, 10))

### Import a Function from Another Module

    from statistics import mean

    marks = [70, 80, 90]
    print(mean(marks))

Output:

    80

## Packages in Python

A package organizes related Python modules in a directory.

Example structure:

    my_package/
        __init__.py
        addition.py
        subtraction.py

Here, `addition.py` and `subtraction.py` are modules inside the package. The `__init__.py` file can be used to mark a directory as a regular Python package.

Modules and packages help organize and reuse code in larger programs.