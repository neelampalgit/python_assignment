def sum_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

print(sum_digits(123))  # Output: 6
