# Task 3
# Create a function called make_operation
# which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
# and an arbitrary number of arguments (only numbers)
# as the second parameter.
# Then return the sum or product of all the numbers
# in the arbitrary parameter.

from operator import sub
from functools import reduce


def make_operation(operator, *args):
    total = 1
    if operator == '+':
        print(sum(args))
    elif operator == '-':
        print(reduce(sub, args))
    elif operator == '*':
        for multiply in args:
            total *= multiply
        print(total)
    else:
        print("Use only '+', '-', '*' operators")


make_operation('+', 7, 7, 2)
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 6)
