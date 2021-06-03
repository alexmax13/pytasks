# Task 1
# Create a function called make_country
# which takes in a country’s name
# and capital as parameters
# create a dictionary from those two
# Make the function print out the values

dic_country = {}


def dict_func(country, capital):
    dic_country[country] = capital
    print(dic_country)


dict_func("Germany", "Berlin")
dict_func("Ukraine", "Kiev")
