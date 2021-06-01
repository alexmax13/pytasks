# Task 3
# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10
# `j` is corresponding to `i` squared
a = range(1, 11)
list_1 = [(i, j**2) for i, j in a]
print(list_1)
