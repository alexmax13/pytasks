# Task 3
import random
count = 0
limit = 5
var_1 = (input('Insert the word:'))
while count < limit:
    var_2 = random.sample(var_1, len(var_1))
    print("".join(var_2))
    count += 1
