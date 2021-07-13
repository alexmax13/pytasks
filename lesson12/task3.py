# Task 3

# Create a Fraction class, which will represent all basic
# arithmetic logic for fractions (+, -, /, *) with appropriate checking and error handling

class MyFraction:
    def __init__(self, numerator, denominator):
        if type(numerator) is not int:
            raise TypeError
        elif type(denominator) is not int:
            raise TypeError
        elif denominator == 0:
            raise ZeroDivisionError

        self.numerator = numerator
        self.denominator = denominator

        if self.numerator % self.denominator == 0:
            self.numerator //= self.denominator
            self.denominator //= self.denominator
        elif self.denominator % self.numerator == 0:
            self.denominator //= self.numerator
            self.numerator //= self.numerator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __mul__(self, other):
        return MyFraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __add__(self, other):
        den_self = self.denominator
        den_other = other.denominator
        return MyFraction(self.numerator * den_other + other.numerator * den_self, den_self * den_other)

    def __sub__(self, other):
        return MyFraction(self.numerator * other.denominator - self.denominator * other.numerator,
                          self.denominator * other.denominator)

    def __truediv__(self, other):
        return MyFraction(self.numerator * other.denominator, self.denominator * other.numerator)


x = MyFraction(1, 2)
y = MyFraction(1, 4)

print(x + y)
print(x * y)
print(x - y)
print(x / y)


