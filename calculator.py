"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def logarithm(argument, base):
    if argument <= 0:
        raise ValueError("Invalid argument")
    if base <= 0 or base == 1:
        raise ValueError("Invalid base")
    return math.log(argument, base)

def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def square_root(n):
    if n < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(n)