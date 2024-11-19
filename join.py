list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# another way to join list is by appending
for x in list2:
    list1.append(x)
print(list1)

list1.append(list2)
print(list1)
