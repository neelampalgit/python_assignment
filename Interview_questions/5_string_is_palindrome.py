def second_largest(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2] if len(arr) > 1 else None

arr = [1, 2, 3, 4, 5]
print(second_largest(arr))  # Output: 4
