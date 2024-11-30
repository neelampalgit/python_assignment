def find_pairs(arr, target):
    pairs = []
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

print(find_pairs([1, 2, 3, 4, 5], 5))  # Output: [(1, 4), (2, 3)]
