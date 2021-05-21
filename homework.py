#  Task 1
str_1 = 'helloworld'
a = str_1[0:2]
b = str_1[8:]
print(a + b)

str_2 = 'my'
print(str_2 * 2)

str_3 = 'x'
if len(str_3) < 2:
    print('')
else:
    print(str_3)

#  Task 2
phone_number = "123456789n"
check_var = phone_number.isdigit()
if check_var is not True:
    print('It doesn\'t look like a phone number')
else:
    print("It\'s a phone number!")

#  Task 3
my_name = 'sasha'
name_input = input('Please, enter your name:')
if name_input.lower() == my_name:
    print(True)
else:
    print(False)
