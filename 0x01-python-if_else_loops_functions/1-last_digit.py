#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    last = -1 * (abs(number) % 10)
else:
    last = number % 10
if last > 5:
    print(f'Last digit of {number} is {last} and is greater than 5')
elif last == 0:
    print(f'Last digit of {number} is {last} and is 0')
else:
    print(f'Last digit of {number} is {last} and is less than 6 and not 0')
