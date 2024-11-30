def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

arr = [1, 2, 4, 5]
print(find_missing_number(arr, 5))  # Output: 3
