myList = ["apple", "Banana", "cherry", "apple"]
# Lists are used to store multiple items in a single variable.
print(myList)

# to determine how many items in the list we use len()
print(len(myList))


# A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# Using the list() constructor to make a List:
list2 = list(("apple", "cherry", "grapes", "mellon"))
print(list2)

# Access List Items
print(list2[-1])
"""Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc"""
# Range of indexes
print(list2[1:3])
# Change list
list2[1] = "Avocado"
print(list2)

# The insert() method inserts an item at the specified index:
list4 = ["Apple", "Banana", "Grapes", "cherry"]
list4.insert(2, "watermelon")
print(list4)
# append , to add the value in the list but take the last spot
list4.append("orange")
print(list4)


# extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove List items

# we iuse remove()
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index.
thislist.pop(1)
print(thislist)
# If you do not specify the index, the pop() method removes the last item.
thislist.pop()
print(thislist)

# again del remove the specified index
del thislist[0]
print(thislist)
thislist = ["apple", "banana", "cherry"]
# del thislist
# # delete the intire list
# print(thislist)


# The clear() method empties the list
# The clear() methad empty the list
# the list still remain but has no comtent
thislist.clear()
print(thislist)
