

def mult(a: int, n: int):
    if n < 0:
        raise ValueError("This function works only with positive integers")
    if n == 0:
        return n
    return a + mult(a, n - 1)


print(mult(2, 4))

print(mult(2, 0))

mult(2, -4)
