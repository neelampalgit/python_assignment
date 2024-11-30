def rotate_array(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
print(rotate_array(arr, 2))  # Output: [4, 5, 1, 2, 3]
