def with_index(iterable, start=0):
    n = start
    for element in iterable:
        yield n, element
        n += 1


week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(list(with_index(week, start=1)))
