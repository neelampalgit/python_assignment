def reverse_words(s):
    # Split the string into words, reverse the list of words, and join them back into a string
    words = s.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

# Example usage:
print(reverse_words("The sky is blue"))  # Output: "blue is sky The"
