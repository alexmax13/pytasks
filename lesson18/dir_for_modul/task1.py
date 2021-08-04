def with_index(iterable, start=0):
    n = start
    for element in iterable:
        yield n, element
        n += 1



