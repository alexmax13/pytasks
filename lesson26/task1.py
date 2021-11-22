
class Stack:
    def __init__(self):
        self.__container = []

    def pop(self):
        return self.__container.pop()

    def push(self, element):
        self.__container.append(element)

    def __len__(self):
        return len(self.__container)


def reverse_str(string: str):
    stack = Stack()
    reversed_string = ""
    for i in string:
        stack.push(i)
    while len(stack):
        reversed_string += stack.pop()
    return reversed_string


print(reverse_str("karina"))
