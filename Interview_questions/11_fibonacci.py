def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]