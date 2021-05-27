# Task 1
# get the largest number from a list of random numbers
# length of 10

import random
count = 0
list_1 = []
while count <= 10:
    list_1.append(random.randint(1, 301))
    count += 1
print(list_1)
print("The largest number from a list:", max(list_1))
