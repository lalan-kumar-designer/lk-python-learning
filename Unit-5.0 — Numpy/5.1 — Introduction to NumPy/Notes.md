# Introduction to NumPy

## Introduction

NumPy stands for Numerical Python. It is a Python library used for numerical calculations and working with arrays.

NumPy provides an efficient way to store and process numerical data.

## What is NumPy?

NumPy is a Python library that provides support for arrays and mathematical operations on array data.

It is commonly used for numerical calculations and scientific computing.

## Importing NumPy

To use NumPy in a Python program, we import it using the `import` keyword.

    import numpy as np

Here, `np` is the commonly used alias for NumPy.

## Creating a NumPy Array

The `np.array()` function is used to create a NumPy array from a list or other supported sequence.

Example:

    import numpy as np

    arr = np.array([10, 20, 30, 40, 50])

    print(arr)

Output:

    [10 20 30 40 50]

## Displaying an Array

A NumPy array can be displayed using the `print()` function.

    import numpy as np

    numbers = np.array([5, 10, 15, 20])

    print("Array:", numbers)

Output:

    Array: [ 5 10 15 20]

## Checking the Type of an Array

The built-in `type()` function returns the type of an object.

    import numpy as np

    arr = np.array([1, 2, 3])

    print(type(arr))

Output:

    <class 'numpy.ndarray'>

Here, `ndarray` is NumPy's main array data structure.

## NumPy Array and Python List

A Python list can store a collection of elements. NumPy arrays are designed for efficient numerical operations.

Example:

    import numpy as np

    numbers = np.array([10, 20, 30])

    print(numbers + 5)

Output:

    [15 25 35]

The value `5` is added to every element of the NumPy array.

## Basic Array Operations

NumPy allows arithmetic operations to be performed on array elements.

    import numpy as np

    arr = np.array([10, 20, 30, 40])

    print("Array:", arr)
    print("Addition:", arr + 5)
    print("Multiplication:", arr * 2)

Output:

    Array: [10 20 30 40]
    Addition: [15 25 35 45]
    Multiplication: [20 40 60 80]

## Comparing Array Elements

Comparison operations check each element and return `True` or `False`.

    import numpy as np

    arr = np.array([10, 20, 30, 40, 50])

    print(arr > 25)
    print(arr == 30)
    print(arr < 40)

Output:

    [False False  True  True  True]
    [False False  True False False]
    [ True  True  True False False]

## Complete Program

    import numpy as np

    arr = np.array([10, 20, 30, 40, 50])

    print("Array:", arr)
    print("Type:", type(arr))
    print("Array + 5:", arr + 5)
    print("Array * 2:", arr * 2)
    print("Elements greater than 25:", arr > 25)
