# Length of Last Word
#     Problem: Given a string s, return the length of the last word in the string. A word is defined as a sequence of non-space characters.
#     Example: "Hello World" → 5.

def length_of_last_word(s):
    return len(s.strip().split()[-1])

# Example usage:
print(length_of_last_word("Hello World"))  # Output: 5
