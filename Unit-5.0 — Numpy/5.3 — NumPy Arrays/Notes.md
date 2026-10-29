A NumPy array is the fundamental data structure of NumPy. It is used to store and process numerical data in Python.

NumPy arrays can have one or more dimensions.

## Creating NumPy Arrays

NumPy provides different methods to create arrays, such as `np.array()`, `np.zeros()` and `np.ones()`.

### Creating an Array Using `np.array()`

The `np.array()` function creates a NumPy array from a Python list.

**Example:**

    import numpy as np

    arr = np.array([10, 20, 30, 40, 50])

    print(arr)

**Output:**

    [10 20 30 40 50]

### Creating an Array Using `np.zeros()`

The `np.zeros()` function creates an array filled with zeros.

**Example:**

    import numpy as np

    arr = np.zeros(5)

    print(arr)

**Output:**

    [0. 0. 0. 0. 0.]

### Creating an Array Using `np.ones()`

The `np.ones()` function creates an array filled with ones.

**Example:**

    import numpy as np

    arr = np.ones(5)

    print(arr)

**Output:**

    [1. 1. 1. 1. 1.]

## NumPy Array Attributes

Array attributes provide information about a NumPy array.

### Shape

The `shape` attribute returns the size of the array along each dimension.

**Example:**

    import numpy as np

    arr = np.array([10, 20, 30, 40, 50])

    print(arr.shape)

**Output:**

    (5,)

### Size

The `size` attribute returns the total number of elements in an array.

**Example:**

    import numpy as np

    arr = np.array([10, 20, 30, 40, 50])

    print(arr.size)

**Output:**

    5

### Dimensions (`ndim`)

The `ndim` attribute returns the number of dimensions of an array.

**Example:**

    import numpy as np

    arr = np.array([10, 20, 30, 40, 50])

    print(arr.ndim)

**Output:**

    1

## Complete Python Program

**File Name:** `numpy_arrays.py`

    import numpy as np

    arr = np.array([10, 20, 30, 40, 50])
    zeros_arr = np.zeros(5)
    ones_arr = np.ones(5)

    print("NumPy Array:", arr)
    print("Zeros Array:", zeros_arr)
    print("Ones Array:", ones_arr)

    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print("Dimensions:", arr.ndim)

**Output:**

    NumPy Array: [10 20 30 40 50]
    Zeros Array: [0. 0. 0. 0. 0.]
    Ones Array: [1. 1. 1. 1. 1.]
    Shape: (5,)
    Size: 5
    Dimensions: 1

## Important Points

- A NumPy array is the fundamental data structure of NumPy.
- `np.array()` creates an array from a Python list.
- `np.zeros()` creates an array filled with zeros.
- `np.ones()` creates an array filled with ones.
- `shape` returns the size along each dimension.
- `size` returns the total number of elements.
- `ndim` returns the number of dimensions.
