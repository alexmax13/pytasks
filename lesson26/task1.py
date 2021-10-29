def reverse_str(string: str):
    stack = []
    reversed_string = ""
    for i in string:
        stack.append(i)
    while len(stack):
        reversed_string += stack.pop()
    return reversed_string


print(reverse_str("karina"))
