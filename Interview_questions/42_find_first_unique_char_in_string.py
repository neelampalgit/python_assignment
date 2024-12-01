# Find the First Unique Character in a String
#     Problem: Given a string s, find the first non-repeating character. If none exists, return -1.
#     Example: "loveleetcode" → v.

def first_unique_char(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return -1

# Example usage:
print(first_unique_char("loveleetcode"))  # Output: "v"
