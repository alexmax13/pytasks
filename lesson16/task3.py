# Create your own implementation of an iterable,
# which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


class MyIter:
    def __init__(self, my_list):
        self.list = my_list
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if self.index >= len(self.list):
            raise StopIteration

        return self.list[self.index]

    def __getitem__(self, item):
        return self.list[item - 1]


in_iter = MyIter(week)

print(in_iter[7], end='\n'*2)

for i in in_iter:
    print(i)
