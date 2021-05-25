# Task 1

import random
secret_number = random.randint(1, 10)
while True:
    try:
        guess = int(input('Guess the number:'))
        if guess == secret_number:
            print('You won, it was number', secret_number)
            break
    except ValueError:
        print("This is not an integer, try again")
    else:
        print('You failed, it was number', secret_number)
        break

