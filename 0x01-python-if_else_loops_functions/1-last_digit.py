#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
output = "Last digit of {} is {} and is ".format(number, digit)
if digit > 5:
    out += "greater than 5"
elif digit == 0:
    output += "0"
else:
    output += "less than 6 and not 0"
print(output)
