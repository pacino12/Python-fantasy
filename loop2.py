"""
VACCINES = ["Moderna", "Phizer", "Sputnik v", "Covaxin", "ASTRAZENEKA"]
# nested for loop
for vac in VACCINES:
    print("")
    print("I would like to take a shot of ")
    for i in vac:
        print(i)
        
"""

import time
x = 2
while x < 5:
    print("Value of X is : ", x)
    print("Looping")
    x += 2  # Inclement it
    time.sleep(1)
