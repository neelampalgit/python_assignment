def union(arr1, arr2):
    return list(set(arr1) | set(arr2))

arr1 = [1, 2, 3]
arr2 = [3, 4, 5]
print(union(arr1, arr2))  # Output: [1, 2, 3, 4, 5]
