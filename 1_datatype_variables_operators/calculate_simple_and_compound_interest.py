def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal

p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time period: "))

print("Simple Interest:", calculate_simple_interest(p, r, t))
print("Compound Interest:", calculate_compound_interest(p, r, t))
