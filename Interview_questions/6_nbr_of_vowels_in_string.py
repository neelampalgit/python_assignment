def count_vowels(s):
    return sum(1 for char in s if char in "aeiouAEIOU")

print(count_vowels("hello"))  # Output: 2
