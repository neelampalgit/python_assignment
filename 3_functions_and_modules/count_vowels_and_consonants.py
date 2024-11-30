def count_vowels_consonants(s):
    vowels = "aeiou"
    vowels_count = consonants_count = 0
    for char in s.lower():
        if char in vowels:
            vowels_count += 1
        elif char.isalpha():
            consonants_count += 1
    return vowels_count, consonants_count

string = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(string)
print(f"Vowels: {vowels}, Consonants: {consonants}")
