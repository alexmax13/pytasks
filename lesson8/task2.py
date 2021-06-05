# Task 2
# Write a function that takes in two numbers from the user via input
# call the numbers a and b, and then returns the value of squared a
# divided by b, construct a try-except block which
# raises an exception if the two values given by the input
# function were not numbers, and if value b was zero (cannot divide by zero)


def math_func(a, b):
    try:
        i = (int(a) ** 2) / int(b)
        print("The result will be:", float(i))
    except ValueError:
        print("Try to insert the number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")


x = input("Insert first number:")
y = input("Insert second number:")
math_func(x, y)
