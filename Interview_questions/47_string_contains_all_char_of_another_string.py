# Check if a String Contains All Characters of Another String
#     Problem: Given two strings s1 and s2, check if s1 contains all characters of s2.
#     Example: s1 = "abcde", s2 = "ace" → True

def contains_all_chars(s1, s2):
    return all(s1.count(c) >= s2.count(c) for c in s2)

# Example usage:
print(contains_all_chars("abcde", "ace"))  # Output: True
