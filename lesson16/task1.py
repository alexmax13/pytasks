# Create your own implementation of a built-in function enumerate,
# named `with_index`, which takes two parameters:
# `iterable` and `start`, default is 0.
#
# Tips: see the documentation for the enumerate function

def with_index(iterable, start=0):
    n = start
    for element in iterable:
        yield n, element
        n += 1


week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# print(list(with_index(week, start=1)))            # or

for i in with_index(week, start=1):
    print(i)
