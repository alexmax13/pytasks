#  Task 1

name = "Sasha"
day = " Monday"
message = f'Good day, {name}!\
{day} is a perfect day to learn some python.'
print(message, end='\n\n\n')

#  Task 2

first_name = 'Sasha'
last_name = ' Maksiutynskyi'
msg_1 = f'{first_name} {last_name} is a coder!'
msg_2 = first_name + last_name + ' is a coder!'
print(msg_1, end='\n\n')
print(msg_2, end='\n\n')


#  Task 3

a = 5
b = 2
print(
    a + b,   # Addition
    a - b,   # Subtraction
    a * b,   # Multiplication
    a / b,   # Division
    a // b,  # Floor division
    a % b,   # Modulus
    a ** b,  # Exponent
    sep='\n'
     )
