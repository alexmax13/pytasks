# Task 1

# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!


def logger(func):
    def wrap(*args, **kwargs):
        print(f'The result will be: {func(*args, **kwargs)}')
    return wrap


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)

square_all(8, 6, 2, 4, 1)

