# Count Substring Occurrences in a String:
#     Problem: Given a string s and a substring sub, count the number of occurrences
#     of sub in s.
#     Example: "ababab", "ab" → 3.

def count_substring_occurrences(s, sub):
    return s.count(sub)

# Example usage:
print(count_substring_occurrences("ababab", "ab"))  # Output: 3
