mytuple = ("apple", "banana", "cherry")

# Ordered
# Unchangeble
print(mytuple[1])
list = list(mytuple)
list[1] = "berry"
print(tuple(list))

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
