# We loop through list items by using for
import time
rich = ["buggati", "rollsroyce", "ferari"]
# so let see if i can get all the items by using for
for i in rich:
    print(i)
# Cowabanga

# Lets loop through the index numbers
for i in range(len(rich)):
    print(rich[i])


# Lets dive in with while loop
print("###############")
rich = ["buggati", "rollsroyce", "ferari"]
i = 0
while i < len(rich):
    print(rich[i])
    i = i+1
time.sleep(3)
print("Looping Using List Comprehension")
[print(x) for x in rich]
