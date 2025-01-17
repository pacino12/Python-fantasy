# Stored in tuple thats args
# stored in dictionary thats kwargs
import random


def time_activity(*args, **kwargs):

    print(args)
    print(kwargs)
    min = sum(args) + random.randint(0, 60)
    print(min)
    choice = random.choice(list(kwargs.keys()))
    print(choice)
    print(f"You have to spend {min} minutes for {choice}")


time_activity(10, 20, 30, hobby="Music", sport="Lifting",
              fun="driving", work="devops")
