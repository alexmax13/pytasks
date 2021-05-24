# Task 3
import random
count = 0
limit = 5
word_1 = input('Insert the word:')
while count < limit:
    var_2 = random.sample(word_1, len(word_1))
    print("".join(var_2))
    count += 1
