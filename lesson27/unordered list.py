from copy import copy


class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next


class UnorderedList:

    def __init__(self):
        self._head = None

    def append(self, data):
        new_node = Node(data)
        current = self._head
        if current is None:
            self._head = new_node
            return
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)

    def index(self, index):
        current = self._head
        count = 0
        while current is not None:
            if count == index:
                return current.get_data()
            count += 1
            current = current.get_next()
        print("Index is out of range")
        return None

    def insert(self, index, data):
        new_node = Node(data)
        current = self._head
        count = 0
        while current.get_next is not None:
            if index == 0:
                new_node.set_next(current)
                self._head = new_node
                return
            elif count + 1 == index:
                next_node = current.get_next()
                current.set_next(next_node)
                new_node.set_next(next_node)
                return
            count += 1
            current = current.get_next()
        print('Index is out of range')

    def pop(self):
        pop_node = self._head
        self._head = self._head.get_next()
        pop_node.get_next = None
        return pop_node._data

    def slice(self, start, stop):
        if start and stop < 0:
            return "Index is out of range"
        elif start >= stop:
            return "Incorrect slice"

        # 0. input param validation (start < stop, start\ stop < 0)
        sliced_list = UnorderedList()
        current_node = self._head
        current_index = 0
        while current_node is not None:
            if current_index == start:
                # stopping the loop if found start
                break
            current_index += 1
            current_node = current_node.get_next()
        # 2. make copy of start the head

        # 3.copy next items until the stop
        while current_index < stop:
            copied_data = copy(current_node.get_data())
            sliced_list.append(copied_data)
            current_index += 1
            current_node = current_node.get_next()
        return sliced_list

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


my_list = UnorderedList()

my_list.append(2)
my_list.append(4)
my_list.append(8)
my_list.append(16)
# my_list.insert(0, 1)
#
# my_list.pop()
# my_list.pop()


# print(my_list.index(20))
new_list = my_list.slice(1, 3)
# my_list.add(31)
# my_list.add(77)
# my_list.add(17)
# my_list.add(93)
# my_list.add(26)
# my_list.add(54)
#
# print(my_list.size())
print(new_list)
print(my_list)
# print(my_list.search(93))
# print(my_list.search(100))
#
# my_list.add(100)
# print(my_list.search(100))
# print(my_list.size())
#
# my_list.remove(54)
# print(my_list.size())
# my_list.remove(93)
# print(my_list.size())
# my_list.remove(31)
# print(my_list.size())
# print(my_list.search(93))
