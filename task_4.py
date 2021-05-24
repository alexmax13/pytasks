# Task 4
while True:
    try:
        math_question = int(input("(2048 / 8 * 24) / 3:"))
        x = (2048 / 8 * 24) / 3
        if math_question == x:
            print("Correct!")
            break
    except ValueError:
        print("This is not an integer, try again")
    else:
        print("Wrong. It's!", int(x))
        break
