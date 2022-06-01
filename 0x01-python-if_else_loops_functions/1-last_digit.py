#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
length = len(str(number))
for i in range(length - 1):
    number = number % 10
print("{:d}".format(number)) 
