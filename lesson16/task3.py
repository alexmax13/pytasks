# Create your own implementation of an iterable,
# which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def my_iter(iterable):
    my_list = iter(iterable)
    return my_list


print('* for loop:'.upper())

for item in my_iter(week):
    print(item)


print('\n', '* next function'.upper())

x = my_iter(week)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# print(next(x))      StopIteration
