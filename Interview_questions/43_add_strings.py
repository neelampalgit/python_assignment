# Add Strings
#     Problem: Given two non-negative integers represented as string,
#     return the sum of these two integers also as a string.
#     Example: "11", "123" → "134".

def add_strings(num1, num2):
    return str(int(num1) + int(num2))

# Example usage:
print(add_strings("11", "123"))  # Output: "134"
