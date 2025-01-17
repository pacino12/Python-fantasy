# # Break statment
# for i in "Devops":
#     print(i)
#     if i == "o":
#         print("I got what i need ")
#         break
# print("Out of loops")

# Skip
# Continiue statment

# for i in "Devops":
#     if i == "o":
#         print("I got what i need ")
#         continue
#     print(f"Value of i is {i}")
# print("Out of loops")
import random
VACCINES = ["Moderna", "Phizer", "Sputnik v", "Covaxin", "ASTRAZENEKA"]
Lucky = random.choice(VACCINES)
print(Lucky)

for vac in VACCINES:
    print(vac)
    if vac == Lucky:
        print(f"{Lucky} vaccine, passed the Test")
        continue
