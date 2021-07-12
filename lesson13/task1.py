# Task 1
# Write a Python program to detect the number of local variables declared in a function.

def func():
    a = 1
    b = 2
    c = 3
    x, y, z, = 4, 5, 6
    str_1 = 'hi'


print(f'Number of local variables: {func.__code__.co_nlocals}')
