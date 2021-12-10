numbers = [2, 3, 4, 10, 40]
looking_num = 4


def fibonacci_search(nums, x):
    size = len(nums)
    start = -1
    fib_min_2 = 0
    fim_min_1 = 1
    fib = 1
    while fib < size:
        fib_min_2 = fim_min_1
        fim_min_1 = fib
        fib = fim_min_1 + fib_min_2

    while fib > 1:
        index = min(start + fib_min_2, size - 1)
        if nums[index] < x:
            fib = fim_min_1
            fim_min_1 = fib_min_2
            fib_min_2 = fib - fim_min_1
            start = index
        elif nums[index] > x:
            fib = fib_min_2
            fim_min_1 = fim_min_1 - fib_min_2
            fib_min_2 = fib - fim_min_1
        else:
            return index
    if fim_min_1 and (nums[size - 1] == x):
        return size - 1
    return -1


result = fibonacci_search(numbers, looking_num)

print(result)
