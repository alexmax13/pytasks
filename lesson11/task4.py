# Task 2

# Create your custom exception named `CustomException`, you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named `logs.txt`.
# Tips: Use __init__ method to extend functionality for saving messages to file

class CustomException(Exception):
    def __init__(self, message):
        with open('logs.txt', 'w') as file:
            file.write(message)


raise CustomException('Random Error')
