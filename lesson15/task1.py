# Create a class method named `validate`, which should be called from the `__init__`
# method to validate parameter email, passed to the constructor.
# The logic inside the `validate` method could be to check
# if the passed email parameter is a valid email string.

import re
regexp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b'


class ValidEmail:
    def __init__(self, email):
        if not self.validate(email):
            raise ValueError('incorrect email')
        self.email = email

    @staticmethod
    def validate(email):
        isvalid = re.match(regexp, email)
        if isvalid:
            print("Valid Email")
        else:
            print("Invalid Email")
        return isvalid


a = ValidEmail('oleksandrmax13@mail.com')
