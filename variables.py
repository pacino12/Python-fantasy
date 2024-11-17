x = 5
y = "Marry"
print(x)
print(y)
# Just like Khaled anather one
x = 4       # x is of type int
x = "Sally"  # x is now of type str
print(x)

# casting
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)  # Here x will be "3"
y = int(3)  # y will be 3
z = float(3)  # z will be 3.

print(x)
print(y)
print(z)
print("Why is this git commands not chilling")
print(y)
# Single or dauble quotes
x = "John"
y = "peter"  # they are the same actually


# what about case sensitive
# well python is case sensitive
a = 4
A = "Sally"
# A will not overwrite a
# Python Variables - Assign Multiple Values
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
"""One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:

"""

x = y = z = "Orange"
print(x)
print(y)
print(z)

"""Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

"""
# Unpack list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#   OUTPUT VARIABLES
x = "python is owesome"
print(x)
x = "Python"
y = "is"
z = "foine"
print(x, y, z)
#  we can use + instead
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Python - Global Variables
# Variables that are created outside of a function
# Example
# Create a variable outside of a function, and use it inside the function

x = "foine"


def myfunc():
    print("Python is " + x)


myfunc()

"""If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value."""

# Example

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)
