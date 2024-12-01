# String Permutation Check#
#     Problem: Given two strings, check if one string is a permutation of the other.
#     Example: s1 = "abc", s2 = "cab" → True.

def is_permutation(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage:
print(is_permutation("abc", "cab"))  # Output: True
