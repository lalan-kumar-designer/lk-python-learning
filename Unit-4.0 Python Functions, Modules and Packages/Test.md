# Unit 4 — Python Functions, Modules and Packages

## Section A — Objective Questions (30 MCQs)

Choose the correct option for each question.

### Questions

**Q1. Which keyword is used to define a function in Python?**

- A. `function`
- B. `def`
- C. `define`
- D. `fun`

**Q2. Which of the following is a built-in function?**

- A. `sqrt()`
- B. `factorial()`
- C. `len()`
- D. `randint()`

**Q3. Which symbols are used to pass arguments when calling a function?**

- A. `[]`
- B. `{}`
- C. `()`
- D. `<>`

**Q4. Which of the following is a user-defined function?**

- A. `print()`
- B. `len()`
- C. A function created using `def`
- D. `type()`

**Q5. What is a parameter?**

- A. A value passed in a function call
- B. A variable in a function definition
- C. A module name
- D. An error message

**Q6. What is an argument?**

- A. A function keyword
- B. A module name
- C. A value passed to a function
- D. A Python package

**Q7. What is a default parameter?**

- A. A parameter with a predefined value
- B. A global variable
- C. A built-in function
- D. A module

**Q8. In positional argument passing, values are assigned according to:**

- A. Data type
- B. Alphabetical order
- C. Position
- D. Variable size

**Q9. Which keyword creates a lambda function?**

- A. `def`
- B. `lambda`
- C. `return`
- D. `global`

**Q10. How many expressions can a lambda function body contain?**

- A. Only one
- B. Two
- C. Three
- D. Unlimited statements

**Q11. Which keyword sends a value back from a function?**

- A. `print`
- B. `send`
- C. `return`
- D. `break`

**Q12. A variable defined inside a function normally has:**

- A. Global scope
- B. Local scope
- C. Module scope only
- D. No scope

**Q13. A variable defined at module level has:**

- A. Local scope
- B. Global scope
- C. Loop scope
- D. Function scope

**Q14. Which keyword allows assignment to a global variable inside a function?**

- A. `public`
- B. `local`
- C. `global`
- D. `static`

**Q15. Which keyword imports a Python module?**

- A. `include`
- B. `import`
- C. `require`
- D. `using`

**Q16. Which module provides mathematical functions?**

- A. `random`
- B. `math`
- C. `datetime`
- D. `re`

**Q17. What is the result of `math.sqrt(36)`?**

- A. `6`
- B. `6.0`
- C. `18`
- D. `36`

**Q18. Which function generates a random integer within a given range?**

- A. `random()`
- B. `randint()`
- C. `sqrt()`
- D. `mean()`

**Q19. Which module is used for dates and times?**

- A. `timeonly`
- B. `calendaronly`
- C. `datetime`
- D. `math`

**Q20. What is the purpose of the `as` keyword during import?**

- A. Delete a module
- B. Create an alias
- C. Stop execution
- D. Handle errors

**Q21. Which module supports regular expressions?**

- A. `re`
- B. `math`
- C. `statistics`
- D. `random`

**Q22. Which `re` function returns all matching occurrences?**

- A. `search()`
- B. `match()`
- C. `findall()`
- D. `sub()`

**Q23. Which function replaces matching text in a string using regular expressions?**

- A. `replaceall()`
- B. `sub()`
- C. `match()`
- D. `fullmatch()`

**Q24. Which regular expression matches one or more digits?**

- A. `\w+`
- B. `\s+`
- C. `\d+`
- D. `\D+`

**Q25. Which block contains code that may raise an exception?**

- A. `except`
- B. `finally`
- C. `try`
- D. `else`

**Q26. Which exception occurs when dividing a number by zero?**

- A. `ValueError`
- B. `TypeError`
- C. `ZeroDivisionError`
- D. `NameError`

**Q27. Which block runs when the `try` block completes without an exception?**

- A. `except`
- B. `else`
- C. `raise`
- D. `import`

**Q28. Which block normally executes whether an exception occurs or not?**

- A. `finally`
- B. `except`
- C. `elif`
- D. `def`

**Q29. What does PyPI stand for?**

- A. Python Program Interface
- B. Python Package Index
- C. Python Programming Index
- D. Package Python Installer

**Q30. Which tool is used to install Python packages?**

- A. `pip`
- B. `print`
- C. `def`
- D. `re`

## Answer Key

| Question | Answer | Question | Answer |
|---|---|---|---|
| 1 | B | 16 | B |
| 2 | C | 17 | B |
| 3 | C | 18 | B |
| 4 | C | 19 | C |
| 5 | B | 20 | B |
| 6 | C | 21 | A |
| 7 | A | 22 | C |
| 8 | C | 23 | B |
| 9 | B | 24 | C |
| 10 | A | 25 | C |
| 11 | C | 26 | C |
| 12 | B | 27 | B |
| 13 | B | 28 | A |
| 14 | C | 29 | B |
| 15 | B | 30 | A |

---

## Section B — Subjective Questions (10)

### Q1. What is a function in Python? Explain its types with examples.

**Answer:**

A function is a block of code that performs a particular task. It helps in code reusability and reduces repetition.

Types of functions:

- Built-in functions: `print()`, `len()`, `sum()`
- Functions defined in modules: `math.sqrt()`, `math.factorial()`
- User-defined functions: Functions created using `def`

Example:

    def greet():
        print("Hello Student")

    greet()

### Q2. Differentiate between arguments and parameters with an example.

**Answer:**

Parameters are variables written in the function definition. Arguments are actual values supplied during the function call.

    def add(a, b):
        print(a + b)

    add(10, 20)

Here, `a` and `b` are parameters, while `10` and `20` are arguments.

### Q3. Explain default parameters and positional arguments with examples.

**Answer:**

A default parameter has a predefined value used when no argument is provided.

    def greet(name="Student"):
        print("Hello", name)

    greet()
    greet("Lalan")

Positional arguments are assigned to parameters according to their order.

    def subtract(a, b):
        print(a - b)

    subtract(20, 5)

### Q4. What is a lambda function? Write a Python program using lambda.

**Answer:**

A lambda function is a small anonymous function defined using the `lambda` keyword. It contains a single expression.

Syntax:

    lambda arguments: expression

Example:

    square = lambda x: x * x
    print(square(5))

    add = lambda a, b: a + b
    print(add(10, 20))

### Q5. Explain the `return` statement in Python with an example.

**Answer:**

The `return` statement sends a value back to the caller. The returned value can be stored in a variable or used in another calculation.

    def multiply(a, b):
        return a * b

    result = multiply(5, 4)
    print("Product:", result)

### Q6. Differentiate between local scope and global scope with an example.

**Answer:**

A local variable is defined inside a function and is normally accessible only within that function. A global variable is defined outside functions at module level.

    x = 100

    def display():
        y = 50
        print("Local:", y)
        print("Global:", x)

    display()
    print(x)

The `global` keyword can be used when a function needs to assign a new value to a global variable.

### Q7. What is a Python module? Explain different ways to import modules.

**Answer:**

A module is a Python file containing reusable functions, variables and other code.

Importing a complete module:

    import math
    print(math.sqrt(25))

Importing a specific function:

    from math import factorial
    print(factorial(5))

Importing with an alias:

    import math as m
    print(m.sqrt(64))

### Q8. What are regular expressions? Explain `search()`, `findall()` and `sub()`.

**Answer:**

Regular expressions are patterns used to search, match and replace text. Python provides the `re` module for this purpose.

    import re

    text = "Python 123 Python"

    print(re.search("Python", text).group())
    print(re.findall(r"\d+", text))
    print(re.sub("Python", "Java", text))

- `search()` finds the first match.
- `findall()` returns all matches.
- `sub()` replaces matching text.

### Q9. Explain exception handling in Python using `try`, `except`, `else` and `finally`.

**Answer:**

Exception handling manages errors that occur during program execution.

- `try` contains code that may raise an exception.
- `except` handles a specified exception.
- `else` runs if no exception occurs.
- `finally` normally executes whether an exception occurs or not.

Example:

    try:
        a = int(input("Enter a number: "))
        print(10 / a)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid input.")
    else:
        print("Calculation successful.")
    finally:
        print("Program completed.")

### Q10. What are PyPI and pip? Explain how to install and import a Python package.

**Answer:**

PyPI stands for Python Package Index. It is an online repository of Python packages.

`pip` is a package manager used to install and manage Python packages.

Check the pip version in the terminal:

    python -m pip --version

Install the `requests` package:

    python -m pip install requests

Use the installed package:

    import requests

    response = requests.get("https://example.com")
    print(response.status_code)

The `requests` package must be installed before it can be imported.

A module is generally a single Python file, while a package organizes related modules.