# Task 3
import random
count = 0
limit = 5
while True:
    word_1 = input('Insert the word:')
    word_check = word_1.isalpha()
    if word_check is False:
        continue
    else:
        while count < limit:
            var_2 = random.sample(word_1, len(word_1))
            print("".join(var_2))
            count += 1
        break
