

def to_power(x, exp: int):
    if exp < 0:
        raise ValueError
    if exp == 0:
        return 1
    left_over = to_power(x, exp - 1)
    return x * left_over


print(to_power(2, 3))

print(to_power(3.5, 2))

print(to_power(2, -1))
