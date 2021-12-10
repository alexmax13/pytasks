numbers = [2, 3, 4, 10, 40]
looking_num = 40


def binary_search(nums, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            return binary_search(nums, low, mid - 1, x)
        else:
            return binary_search(nums, mid + 1, high, x)
    else:
        return -1


result = binary_search(numbers, 0, len(numbers) - 1, looking_num)

print(result)
