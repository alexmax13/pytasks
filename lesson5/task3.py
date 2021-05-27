# Task 3
# Make a list that contains all integers from 1 to 100
# find all integers from the list that are divisible by 7
# find all integers from the list that not  multiple of 5
count = 1
list_1 = []
list_2 = []
while count <= 100:
    list_1.append(count)
    if count % 7 == 0 and count % 5 != 0:
        list_2.append(count)
    count += 1
print(list_1, list_2, sep="\n")
