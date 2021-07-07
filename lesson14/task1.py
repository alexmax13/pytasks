# Task 1

# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!


def logger(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        arguments = [arg for arg in args] + [f'{key}={kwargs[key]}' for key in kwargs]
        last_element = arguments[len(arguments) - 1]

        print(f'{func.__name__}(', end='')
        for arg in arguments:
            print(arg, end='')
            if arg != last_element:
                print(', ', end='')
        print(f') = {result}')

    return wrap


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args, **kwargs):
    return [arg ** 2 for arg in args] + [arg ** 2 for arg in kwargs.values()]


add(4, 5)

square_all(8, 6, 2, 4, b=1)
