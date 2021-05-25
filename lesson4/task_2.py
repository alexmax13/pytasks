# Task 2

name = input("Please enter your name:")
while True:
    try:
        age = int(input("Please enter your age:"))
    except ValueError:
        print("This is not an integer, try again.")
    else:
        print('Hello', name, 'on your next birthday \
you’ll be', age + 1, 'years')
        break
