# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain

# If some of the rules' checks returns False, the function should return False
# and print the reason it failed; otherwise, return the result.


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper_function(*args, **kwargs):
            arguments = []
            arguments.extend(list(args))
            arguments.extend(list(kwargs.values()))
            for arg in arguments:
                if type(arg) != type_:
                    print(f"Incorrect type: {arg}! Required: {type_}")
                    return False
                if len(arg) > max_length:
                    print(f"Incorrect length: {arg}! Required: {max_length}")
                    return False
                for item in contains:
                    if item not in arg:
                        print(f"Missing {item} in {arg}!")
                        return False
            return func(*args, **kwargs)
        return wrapper_function
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new Volvo!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new Volvo!'

