## 1. Introduction to Functions

A function is a block of code that performs a specific task. Functions help us reuse code and make programs easier to understand.

### Advantages of Functions

- Code reusability
- Less repetition
- Easy debugging
- Better program organization

## 2. Types of Functions

Python functions are divided into three types:

1. Built-in Functions
2. Functions Defined in a Module
3. User-defined Functions

### 2.1 Built-in Functions

Built-in functions are already available in Python. We can use them directly.

| Function | Purpose | Example |
|---|---|---|
| `print()` | Displays output | `print("Hello")` |
| `len()` | Returns length | `len("Python")` |
| `max()` | Returns maximum value | `max(10, 20, 30)` |
| `min()` | Returns minimum value | `min(10, 20, 30)` |
| `sum()` | Returns sum | `sum([10, 20, 30])` |
| `type()` | Returns data type | `type(10)` |

Example:

    print("Hello World")
    print(len("Python"))
    print(max(10, 20, 30))
    print(min(10, 20, 30))
    print(sum([10, 20, 30]))
    print(type(10))

### 2.2 Functions Defined in a Module

A module is a Python file containing reusable functions and other code. We import a module before using its functions.

Example:

    import math

    print(math.sqrt(25))
    print(math.factorial(5))

Output:

    5.0
    120

Here, `sqrt()` and `factorial()` are functions from the `math` module.

### 2.3 User-defined Functions

User-defined functions are created by the programmer using the `def` keyword.

Syntax:

    def function_name():
        statements

Example:

    def greet():
        print("Hello Student")

    greet()

Here:
- `def` defines a function.
- `greet` is the function name.
- `greet()` calls the function.

## 3. Arguments and Parameters

A parameter is a variable written inside the parentheses of a function definition.

An argument is the actual value passed to a function when it is called.

Example:

    def add(a, b):
        print(a + b)

    add(10, 20)

Here:
- `a` and `b` are parameters.
- `10` and `20` are arguments.

Example with a string:

    def greet(name):
        print("Hello", name)

    greet("Lalan")

Output:

    Hello Lalan

## 4. Default Parameters

A default parameter has a predefined value. If no argument is provided for it, the default value is used.

Example:

    def greet(name="Student"):
        print("Hello", name)

    greet()
    greet("Lalan")

Output:

    Hello Student
    Hello Lalan

Example with two parameters:

    def add(a, b=10):
        print(a + b)

    add(5)
    add(5, 20)

Output:

    15
    25

Parameters with default values are generally placed after parameters without default values.

## 5. Positional Parameters

In positional argument passing, values are assigned to parameters according to their position in the function call.

Example:

    def student(name, age):
        print("Name:", name)
        print("Age:", age)

    student("Lalan", 17)

Output:

    Name: Lalan
    Age: 17

Example showing the importance of order:

    def subtract(a, b):
        print(a - b)

    subtract(20, 5)
    subtract(5, 20)

Output:

    15
    -15

The order of arguments affects the result.

## 6. Lambda Functions

A lambda function is a small anonymous function created using the `lambda` keyword.

Syntax:

    lambda arguments: expression

Example 1: Addition

    add = lambda a, b: a + b
    print(add(10, 20))

Output:

    30

Example 2: Square

    square = lambda x: x * x
    print(square(5))

Output:

    25

Example 3: Multiplication

    multiply = lambda a, b: a * b
    print(multiply(4, 5))

Output:

    20

A lambda function can contain multiple arguments but only one expression.

## 7. Returning Value

The `return` statement sends a value back from a function to the place where it was called.

Example 1: Addition

    def add(a, b):
        return a + b

    result = add(10, 20)
    print(result)

Output:

    30

Example 2: Square

    def square(number):
        return number * number

    print(square(5))

Output:

    25

Example 3: Area of a Rectangle

    def calculate_area(length, width):
        return length * width

    area = calculate_area(5, 4)
    print("Area:", area)

Output:

    Area: 20

### Difference Between `print()` and `return`

- `print()` displays a value on the screen.
- `return` sends a value back to the caller.
- A returned value can be stored in a variable and used in further calculations.

## 8. Scope of a Variable

Variable scope determines where a variable can be accessed in a program.

There are two types:

1. Local Scope
2. Global Scope

### 8.1 Local Scope

A local variable is created inside a function. It is normally accessible only within that function.

Example:

    def display():
        y = 50
        print(y)

    display()

Output:

    50

Here, `y` is a local variable.

### 8.2 Global Scope

A global variable is defined outside a function. It can be accessed inside functions, provided it is not shadowed by a local variable of the same name.

Example:

    x = 100

    def display():
        print(x)

    display()
    print(x)

Output:

    100
    100

Here, `x` is a global variable.

### 8.3 Local and Global Variables with the Same Name

    a = 10

    def show():
        a = 20
        print("Local a:", a)

    show()
    print("Global a:", a)

Output:

    Local a: 20
    Global a: 10

The local variable `a` does not change the global variable `a`.

### 8.4 Using the `global` Keyword

The `global` keyword allows a function to assign a new value to a global variable.

Example:

    number = 5

    def change():
        global number
        number = 15

    change()
    print(number)

Output:

    15