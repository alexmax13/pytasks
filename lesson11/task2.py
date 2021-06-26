# Task 2

# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# - square_nums (takes a list of integers and returns the list of squares)
# - remove_positives (takes a list of integers and returns it without positive numbers
# - filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:

    def square_nums(self, lst):
        squares = []
        for i in lst:
            squares.append(i ** 2)
        return squares

    def remove_positives(self, lst):
        pos_num = [num for num in lst if num < 0]
        return pos_num

    def filter_leaps(self, lst):
        import calendar
        leaps = [i for i in lst if calendar.isleap(i)]
        return leaps


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

