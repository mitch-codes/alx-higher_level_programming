#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mynumber = number
if mynumber < 0:
    mynumber = mynumber * -1
length = len(str(mynumber))
for i in range(length - 1):
    mynumber = mynumber % 10
if number < 0:
    mynumber = mynumber * -1
if mynumber > 5:
    print("Last digit of {:d} is {:d} ".format(number, mynumber), end="")
    print("and is greater than 5")
elif mynumber < 6 and mynumber != 0:
    print("Last digit of {:d} is {:d} ".format(number, mynumber), end="")
    print("and is less than 6 and not 0")
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, mynumber))
