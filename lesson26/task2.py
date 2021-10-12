
parentheses_list = input()
stack = []
is_balanced = True
for i in parentheses_list:
    if i in "([{":
        stack.append(i)
    elif i in ")]}":
        if not stack:
            is_balanced = False
            break
        open_bracket = stack.pop()
        if open_bracket == "(" and i == ")":
            continue
        if open_bracket == "[" and i == "]":
            continue
        if open_bracket == "{" and i == "}":
            continue
        is_balanced = False
        break
if is_balanced and len(stack) == 0:
    print("Balanced")
else:
    print("Not balanced")
