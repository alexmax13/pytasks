# Task 2
# Generate 2 lists with the length of 10 with random integers
# make a third list containing the common integers

import random
count = 0
list_1 = []
list_2 = []
list_common = []
while count <= 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))
    count += 1
common_var = list(set(list_1) and set(list_2))
list_common.append(common_var)
print(list_1, list_2, common_var, sep="\n")
