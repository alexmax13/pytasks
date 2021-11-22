
class Stack:
    def __init__(self):
        self.__container = []

    def __str__(self):
        return str(self.__container)

    def pop(self):
        return self.__container.pop()

    def push(self, element):
        self.__container.append(element)

    def __len__(self):
        return len(self.__container)

    def get_from_stack(self, element):
        for i in self.__container:
            if i == element:
                self.__container.remove(element)
                return element
        raise ValueError("Not found element")


if __name__ == "__main__":
    def reverse_str(string: str):
        stack = Stack()
        reversed_string = ""
        for i in string:
            stack.push(i)
        while len(stack):
            reversed_string += stack.pop()
        return reversed_string


    print(reverse_str("karina"))

    a = Stack()
    a.push("a")
    a.push("x")
    a.push("g")
    a.push("k")

    print(a.get_from_stack('a'))
    print(a)
    a.push("h")
    print(a)
    print(a.get_from_stack('h'))
