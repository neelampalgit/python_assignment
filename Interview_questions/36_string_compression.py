def compress_string(s):
    # Initialize the result list to store the compressed version of the string
    compressed = []
    count = 1

    # Traverse through the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1  # Increase count if the current character is the same as the previous one
        else:
            compressed.append(s[i - 1] + str(count))  # Append the character and its count
            count = 1  # Reset the count for the new character

    # Add the last character and its count
    compressed.append(s[-1] + str(count))

    # Join the list into a string and return the smaller one between the compressed string and the original
    compressed_str = ''.join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

# Example usage:
print(compress_string("aabcccccaaa"))  # Output: "a2b1c5a3"
print(compress_string("abcd"))         # Output: "abcd"
