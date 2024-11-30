def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = swap_numbers(a, b)
print("Swapped numbers:", a, b)
