# Task 1
# program that has some sentence
# returns a dict containing all unique words as keys
# and the number of occurrences as values

dict_string = "Use a (list) comprehension. To make A List,\
 that containing tuples!".lower()
replace_chars = "!(),."
for replace_char in replace_chars:
    dict_string = dict_string.replace(replace_char, "")
dict_string = dict_string.split()
dict_string = {x: dict_string.count(x) for x in dict_string}
print(dict_string)
