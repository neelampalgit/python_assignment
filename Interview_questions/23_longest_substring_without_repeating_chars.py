def longest_substring(s):
    char_set = set()
    left = result = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        result = max(result, right - left + 1)
    return result

print(longest_substring("abcabcbb"))  # Output: 3
