## Introduction

Array indexing and slicing are used to access elements and subarrays in NumPy arrays.

- **Indexing:** Accesses a particular element of an array.
- **Slicing:** Accesses a range of elements or a subarray.

## Array Indexing

Indexing is used to access individual elements of an array. In Python, indexing starts from `0`.

### Example

    import numpy as np

    arr = np.array([10, 20, 30, 40, 50])

    print(arr[0])
    print(arr[2])

**Output:**

    10
    30

Here, `arr[0]` accesses the first element, and `arr[2]` accesses the third element.

## Array Slicing

Slicing is used to access a range of elements from an array.

**Syntax:**

    array[start:stop]

The `start` index is included, but the `stop` index is excluded.

### Example

    import numpy as np

    arr = np.array([10, 20, 30, 40, 50])

    print(arr[0:3])
    print(arr[3:5])

**Output:**

    [10 20 30]
    [40 50]

## Multidimensional Array Indexing

A multidimensional array contains elements arranged in rows and columns. Elements can be accessed using row and column indexes.

### Example

    import numpy as np

    arr = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])

    print(arr[0, 1])
    print(arr[1, 2])

**Output:**

    20
    60

Here, `arr[0, 1]` accesses the element in the first row and second column. `arr[1, 2]` accesses the element in the second row and third column.

## Multidimensional Array Slicing

Slicing can also be used to access rows, columns, and subarrays.

### Example

    import numpy as np

    arr = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])

    print(arr[0, :])
    print(arr[:, 0:2])

**Output:**

    [10 20 30]
    [[10 20]
     [40 50]]

- `arr[0, :]` accesses all elements of the first row.
- `arr[:, 0:2]` accesses the first two columns of all rows.

## Difference Between One-Dimensional and Multidimensional Indexing

| One-Dimensional Array | Multidimensional Array |
|---|---|
| Uses one index to access an element. | Uses row and column indexes to access an element in a 2D array. |
| Example: `arr[2]` | Example: `arr[1, 2]` |
| Stores elements in a single sequence. | Stores elements in rows and columns. |

## Complete Python Program

**File Name:** `array_indexing_slicing.py`

    import numpy as np

    arr1 = np.array([10, 20, 30, 40, 50])

    print("One-Dimensional Array:")
    print(arr1)

    print("First Element:", arr1[0])
    print("Third Element:", arr1[2])

    print("First Three Elements:", arr1[0:3])
    print("Last Two Elements:", arr1[3:5])

    arr2 = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])

    print("\nMultidimensional Array:")
    print(arr2)

    print("Element at Row 1, Column 2:", arr2[0, 1])
    print("Element at Row 2, Column 3:", arr2[1, 2])

    print("First Row:", arr2[0, :])

    print("First Two Columns:")
    print(arr2[:, 0:2])

### Output

    One-Dimensional Array:
    [10 20 30 40 50]
    First Element: 10
    Third Element: 30
    First Three Elements: [10 20 30]
    Last Two Elements: [40 50]

    Multidimensional Array:
    [[10 20 30]
     [40 50 60]]
    Element at Row 1, Column 2: 20
    Element at Row 2, Column 3: 60
    First Row: [10 20 30]
    First Two Columns:
    [[10 20]
     [40 50]]

## Important Points

- Indexing accesses individual elements of an array.
- Slicing accesses a range of elements or a subarray.
- Python array indexing starts from `0`.
- The stop index in slicing is excluded.
- One-dimensional arrays use a single index.
- Two-dimensional arrays use row and column indexes.
