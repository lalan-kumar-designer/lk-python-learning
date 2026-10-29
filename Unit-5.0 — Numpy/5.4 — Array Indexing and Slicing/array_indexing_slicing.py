import numpy as np

# One-dimensional array
arr1 = np.array([10, 20, 30, 40, 50])

print("One-Dimensional Array:")
print(arr1)

# Indexing in one-dimensional array
print("First Element:", arr1[0])
print("Third Element:", arr1[2])

# Slicing in one-dimensional array
print("First Three Elements:", arr1[0:3])
print("Last Two Elements:", arr1[3:5])

# Multidimensional array
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nMultidimensional Array:")
print(arr2)

# Indexing in multidimensional array
print("Element at Row 1, Column 2:", arr2[0, 1])
print("Element at Row 2, Column 3:", arr2[1, 2])

# Slicing in multidimensional array
print("First Row:", arr2[0, :])
print("First Two Columns:")
print(arr2[:, 0:2])
