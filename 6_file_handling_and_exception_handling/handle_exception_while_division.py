def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except Exception as e:
        return f"An error occurred: {e}"

a = float(input("Enter numerator: "))
b = float(input("Enter denominator: "))
print("Result:", divide(a, b))
