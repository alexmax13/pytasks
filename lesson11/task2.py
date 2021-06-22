# Task 2

# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# - square_nums (takes a list of integers and returns the list of squares)
# - remove_positives (takes a list of integers and returns it without positive numbers
# - filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:

    @staticmethod
    def square_nums(lst):
        squares = []
        for i in lst:
            squares.append(i ** 2)
        return squares

    @staticmethod
    def remove_positives(lst):
        pos_num = [num for num in lst if num >= 0]
        return pos_num

    @staticmethod
    def filter_leaps(lst):
        import calendar
        leaps = [i for i in lst if calendar.isleap(i)]
        return leaps


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
