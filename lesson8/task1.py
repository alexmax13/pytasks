# Task 1
# Write a function called oops
# that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement
# to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?


def oops():
    raise IndexError


def catch_error():
    try:
        oops()
    except IndexError:
        print("This func catch the error!")


catch_error()