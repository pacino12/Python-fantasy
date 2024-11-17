# Booleans represent one of two values: True or False.

# EXAMPLE
print(10 > 9)
print(10 == 9)
print(10 < 9)

## When you run a condition in an if statement, Python returns True or False:##
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables

print(bool("hello"))
print(bool(15))

# ###Most Values are True##
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

"""Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False."""
# Example
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean


def myFunction():
    return True


print(myFunction())

# wee can also use boolean to check whether objecty is integer or not

x = 200.00
print(isinstance(x, int))
