#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    digit = abs(number) % 10
    else: 
        digit = number % 10
if digit > 5:
    print(f"Last digit and is greater than 5")
elif digit == 0:
    print(f"Last digit and is 0")
    print("0")
else digit is < 6 and not 0
    print(f"Last digit and is less than 6 and not 0")
