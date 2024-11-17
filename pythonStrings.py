"""Strings in python are surrounded by either single quotation marks, or double quotation marks."""
print("Hello")
print('Hello')

"""Quotes Inside Quotes
You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

"""
# Example
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to a Variable
a = "Hello"
print(a)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays

a = "Hello, World!"
print(a[5])

"""Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop."""
for x in "banana":
    print(x)

# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))
"""Check String
To check if a certain phrase or character is present in a string, we can use the keyword ""in.


"""
# eg:
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

"""Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword +not in"""
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

"""Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string."""

b = "Hello , World"
print(b[2:5])
# Get the characters from the start to position 5 (not included):
print(b[:5])


# Slice to the end
# Get the characters from position 2, and all the way to the end:
print(b[2:])

# Negative Indexing
"""Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):"""


# EXAMPLE:
print(b[-5:-2])

# MODIFY STRINGS

# Upper case
# The upper() method returns the string in upper case:
a = " Hello ,my guy"
print(a.upper())

# Lower Case
# The lower() method returns the string in lower case:
print(a.lower())
# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

print(a.strip())

# Replace String
print(a.replace("H", "F"))

# Split String
print(a.split(","))


####### Python - String Concatenation#####

"""To concatenate or to combine two variables you can use "+ """
a = " Hello"
b = " World"
c = a + b
print(c)

# To add a space between them, add a " "
c = a + " " + b
print(c)


####### Python - Format - Strings#####

# But we can combine strings and numbers by using f-strings or the format() method!

age = 34
txt = f"My name is pyguy, and i am {age}"
print(txt)

# Placeholders and Modifiers

"""A placeholder can contain variables, operations, functions, and modifiers to format the value."""
price = 59
txt = f"The price is {price} dollars"
print(txt)
txt = f"The price is {price:.2f} dollers"
print(txt)

# Python escape character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# String method
# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
