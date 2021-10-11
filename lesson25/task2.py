

def is_palindrome(looking_str: str):
    if len(looking_str) < 2:
        return True
    if looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])


print(is_palindrome('mom'))

print(is_palindrome('sasas'))

print(is_palindrome('o'))
