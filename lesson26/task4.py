
class Queue:
    def __init__(self):
        self.__container = []

    def __str__(self):
        return str(self.__container)

    def pop(self):
        if len(self.__container) == 0:
            raise IndexError
        buffer = self.__container[0]
        self.__container.pop(0)
        return buffer

    def push(self, element):
        self.__container.append(element)

    def __len__(self):
        return len(self.__container)

    def get_from_queue(self, element):
        for i in self.__container:
            if i == element:
                self.__container.remove(element)
                return element
        raise ValueError("Not found element")


a = Queue()
a.push("a")
a.push("x")
a.push("g")
a.push("k")

print(a)
print(a.pop())

b = Queue()
print(b.pop())
