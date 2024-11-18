# List objects have a sort() method that will sort the list alphanumerically, ascending, by default

# 1 sort alphabetically

thislist = ["orange", "mango", "kiwi", "pineaple", "Banana"]
thislist.sort()
print(thislist)

# numeric

thislist = [100, 30, 50, 40, 70, 45]
thislist.sort()
print(thislist)

# Sort Descending
#  we use a key word reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


# Customize Sort Function
def myfunc(n):
    return abs(n-50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Case Insensitive Sort

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# reverse Order
thislist.reverse()
print(thislist)
