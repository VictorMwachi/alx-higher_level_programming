#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    stmt = "is positive"
elif number < 0:
    stmt = "is negative"
else:
    stmt = "is zero"
print(f"{number} "+stmt)
