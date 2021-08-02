# Write a class TypeDecorators which has several methods for converting
# results of functions to a specified type (if it's possible):

# methods:
# to_int
# to_str
# to_bool
# to_float


class TypeDecorators:
    @classmethod
    def to_int(cls, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return int(result)
        return wrapper

    @classmethod
    def to_str(cls, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    @classmethod
    def to_bool(cls, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return bool(result)
        return wrapper

    @classmethod
    def to_float(cls, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return float(result)

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_str
def do_integer(integer: int):
    return integer


@TypeDecorators.to_float
def do_float(floater):
    return floater


assert (do_nothing('25')) == 25

assert do_something('True') is True

assert do_integer(25) == '25'

assert (do_float('3.14')) == 3.14
