from math import gcd


def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(lcm(4, 5))  # Output: 20
