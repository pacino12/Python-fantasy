fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for i in fruits:
    if "a" in i:
        newlist.append(i)
print(newlist)

# cowabanga innit

# we can also do this in one line of codes
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Syntax
# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if x != "apple"]
newlist = ['hello' for x in fruits]
print(newlist)
