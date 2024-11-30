def max_min_avg(numbers):
    return max(numbers), min(numbers), sum(numbers) / len(numbers)

# Take input and split into list of strings
numbers = input("Enter numbers separated by spaces: ").split()

# Convert the list of string numbers to floats
numbers = [float(x) for x in numbers]

# Check if the list is empty before proceeding
if numbers:
    maximum, minimum, average = max_min_avg(numbers)
    print(f"Max: {maximum}, Min: {minimum}, Average: {average}")
else:
    print("No numbers entered.")
