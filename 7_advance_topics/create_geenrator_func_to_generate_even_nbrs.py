def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
for num in even_numbers(n):
    print(num)
