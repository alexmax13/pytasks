# Task 1

import random

secret_number = random.randint(1, 10)
# We have only three try to guess.
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = input('Guess the number:')
    guess_count += 1
    if guess == secret_number:
        print('You won, it was number', secret_number)
        break
else:
    print('You failed, it was number', secret_number)