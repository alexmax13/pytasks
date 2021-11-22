from task3 import Stack

parentheses_list = input()
stack = Stack()
is_balanced = True
for i in parentheses_list:
    if i in "([{":
        stack.push(i)
    elif i in ")]}":
        if len(stack) == 0:
            is_balanced = False
            break
        open_bracket = stack.pop()
        is_round = (open_bracket == "(" and i == ")")
        is_square = (open_bracket == "[" and i == "]")
        is_curly = (open_bracket == "{" and i == "}")
        if not is_round and not is_square and not is_curly:
            is_balanced = False
            break
if is_balanced and len(stack) == 0:
    print("balanced")
else:
    print("not balanced")
