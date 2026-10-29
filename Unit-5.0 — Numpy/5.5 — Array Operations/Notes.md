## Introduction

Array operations are used to perform calculations on NumPy arrays. NumPy supports arithmetic operations between arrays of compatible shapes.

## Arithmetic Operations on NumPy Arrays

Consider two NumPy arrays:

- First array: `[10, 20, 30, 40, 50]`
- Second array: `[1, 2, 3, 4, 5]`

### Addition

The `+` operator adds corresponding elements of two arrays.

**Example:**

    arr1 + arr2

**Output:**

    [11 22 33 44 55]

### Subtraction

The `-` operator subtracts corresponding elements of the second array from the first array.

**Example:**

    arr1 - arr2

**Output:**

    [ 9 18 27 36 45]

### Multiplication

The `*` operator multiplies corresponding elements of two arrays.

**Example:**

    arr1 * arr2

**Output:**

    [ 10  40  90 160 250]

### Division

The `/` operator divides corresponding elements of the first array by the second array.

**Example:**

    arr1 / arr2

**Output:**

    [10. 10. 10. 10. 10.]

## Complete Python Program

**File Name:** `array_operations.py`

    import numpy as np

    arr1 = np.array([10, 20, 30, 40, 50])
    arr2 = np.array([1, 2, 3, 4, 5])

    print("First Array:", arr1)
    print("Second Array:", arr2)

    print("Addition:", arr1 + arr2)
    print("Subtraction:", arr1 - arr2)
    print("Multiplication:", arr1 * arr2)
    print("Division:", arr1 / arr2)

### Output

    First Array: [10 20 30 40 50]
    Second Array: [1 2 3 4 5]
    Addition: [11 22 33 44 55]
    Subtraction: [ 9 18 27 36 45]
    Multiplication: [ 10  40  90 160 250]
    Division: [10. 10. 10. 10. 10.]

## Important Points

- NumPy arrays support arithmetic operations.
- `+` is used for addition.
- `-` is used for subtraction.
- `*` is used for multiplication.
- `/` is used for division.
- These operations are performed element by element for arrays of compatible shapes.
