#  Task 2
phone_number = "1234567890"
check_var = phone_number.isdigit()
if not check_var or len(phone_number) != 10:
    print("It doesn't look like a phone number")
else:
    print("It's a phone number!")
