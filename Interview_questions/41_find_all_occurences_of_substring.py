# Find All Occurrences of a Substring:
#     Problem: Given a string s and a substring sub, return the list of all starting indices where the substring sub is found in s.
#     Example: s = "ababcababc", sub = "ab" → [0, 3, 6]

def find_occurrences(s, sub):
    return [i for i in range(len(s)) if s.startswith(sub, i)]

# Example usage:
print(find_occurrences("ababcababc", "ab"))  # Output: [0, 3, 6]
