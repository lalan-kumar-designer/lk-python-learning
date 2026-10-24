# Unit 4.2 — Modules and Packages

## 1. Modules in Python

A module is a Python file that contains functions, variables, and reusable code. We can import a module and use its functions in another program.

### Importing a Module

The `import` keyword is used to import a module.

    import math

    print(math.sqrt(25))
    print(math.factorial(5))

Here, `math` is a Python module. The `sqrt()` function returns the square root, and `factorial()` returns the factorial of a number.

### Importing a Module with an Alias

The `as` keyword gives a module a shorter name.

    import math as m

    print(m.sqrt(64))

### Importing Specific Functions

We can import only the functions we need from a module.

    from math import sqrt, factorial

    print(sqrt(49))
    print(factorial(5))

## 2. Regular Expressions

Regular expressions are used to search, match, and replace text using patterns. Python provides the `re` module for regular expressions.

    import re

### search()

The `search()` function searches for a pattern anywhere in a string.

    text = "Python Programming"
    result = re.search("Python", text)
    print(result.group() if result else "Not Found")

### findall()

The `findall()` function returns all matches of a pattern.

    text = "My marks are 75 and 85"
    print(re.findall(r"\d+", text))

Output:

    ['75', '85']

Here, `\d+` matches one or more digits.

### match()

The `match()` function checks for a match at the beginning of a string.

    text = "Python is easy"
    result = re.match("Python", text)
    print(result.group() if result else "No Match")

### sub()

The `sub()` function replaces matching text.

    text = "I like Java"
    print(re.sub("Java", "Python", text))

Output:

    I like Python

### fullmatch()

The `fullmatch()` function checks whether the entire string matches a pattern.

    text = "12345"
    print(bool(re.fullmatch(r"\d+", text)))

Output:

    True

## 3. Exception Handling

An exception is an error that occurs while a program is running. Python uses `try`, `except`, `else`, and `finally` to handle exceptions.

### try and except

The `try` block contains code that may cause an exception. The `except` block handles the exception.

    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Please enter valid numbers.")

### else

The `else` block runs when no exception occurs in the `try` block.

    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input.")
    else:
        print("Number:", number)

### finally

The `finally` block runs whether an exception occurs or not.

    try:
        print(10 / 2)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    finally:
        print("Program completed.")

## 4. PyPI — Python Package Index

PyPI stands for Python Package Index. It is an online repository where Python packages are published and made available for installation.

Website: https://pypi.org/

A package contains code that can be installed and reused in Python programs.

## 5. pip — Python Package Manager

`pip` is used to install and manage Python packages.

### Check the pip Version

Run this command in the terminal:

    python -m pip --version

### Install a Package

For example, to install the `requests` package:

    python -m pip install requests

### Use the Installed Package

    import requests

    response = requests.get("https://example.com")
    print("Status Code:", response.status_code)

The package must be installed before importing it.

Note: Terminal commands are run in the terminal, not as ordinary Python statements inside a `.py` file.

## 6. Importing Libraries and Functions

A library provides reusable code for specific tasks. Python's standard library includes modules such as `math`, `random`, `datetime`, and `statistics`.

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

### Import Constants and Functions

    from math import pi, pow

    print(pi)
    print(pow(2, 3))

### Import a Function from Another Module

    from statistics import mean

    marks = [70, 80, 90]
    print(mean(marks))

Output:

    80

## 7. Modules and Packages

A module is a single Python file containing reusable code.

A package is a way of organizing related Python modules in a directory.

Modules and packages help organize programs and reuse code.

## 8. Complete Example

    import math
    import random
    import re
    from statistics import mean

    print("Square Root:", math.sqrt(81))
    print("Random Number:", random.randint(1, 10))

    text = "Python 123"
    print("Numbers:", re.findall(r"\d+", text))

    marks = [75, 80, 85]
    print("Average Marks:", mean(marks))