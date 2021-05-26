# Task 4

import random
x = random.randint(1, 44)
y = random.randint(9, 23)
z = random.randint(1, 10)
expression = (x + y) * z
while True:
    math_question = input(f'({x} + {y}) * {z} :')
    check_var = math_question.isdigit()
    if check_var is False:
        print("Try to insert the number!")
        continue
    elif int(math_question) == expression:
        print("Correct!")
        break
    else:
        print("Wrong. It's!", int(expression))
        break
