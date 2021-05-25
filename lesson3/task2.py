#  Task 2
phone_number = "1234567890"
check_var = phone_number.isdigit()
if check_var is not True or len(phone_number) < 10:
    print('It doesn\'t look like a phone number')
else:
    print("It\'s a phone number!")