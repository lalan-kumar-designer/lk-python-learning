# Importing Libraries and Functions

# Import a complete module.
import math

print(math.sqrt(36))


# Import specific functions from a module.
from math import sqrt, factorial

print(sqrt(49))
print(factorial(5))


# Import a module using an alias.
import random as r

print(r.randint(1, 10))


# Import multiple functions from the math module.
from math import pi, pow

print(pi)
print(pow(2, 3))


# Import a function from the built-in module.
from statistics import mean

marks = [70, 80, 90]
print(mean(marks))