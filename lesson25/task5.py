

def sum_of_digits(digit_string: str) -> int:
    if digit_string.isalpha():
        raise ValueError("input string must be digit string")
    if digit_string == "":
        return 0
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])


print(sum_of_digits('26'))

print(sum_of_digits('123456789'))

print(sum_of_digits('san'))

