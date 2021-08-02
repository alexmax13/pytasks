# Create your own implementation of a built-in function range,
# named in_range(), which takes three parameters:
# `start`, `end`, and optional step.

# Tips: See the documentation for `range` function

def in_range(start, end, step):
    i = start
    while i < end:
        yield i
        i += step


print(list(in_range(0, 120, 1)))

for item in in_range(0, 120, 1):
    print(item)

