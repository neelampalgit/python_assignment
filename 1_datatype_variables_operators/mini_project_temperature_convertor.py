def temperature_converter():
    temp = float(input("Enter temperature: "))
    unit = input("Enter unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if unit == 'C':
        print(f"{temp}°C = {temp * 9/5 + 32}°F = {temp + 273.15}K")
    elif unit == 'F':
        print(f"{temp}°F = {(temp - 32) * 5/9}°C = {(temp - 32) * 5/9 + 273.15}K")
    elif unit == 'K':
        print(f"{temp}K = {temp - 273.15}°C = {(temp - 273.15) * 9/5 + 32}°F")
    else:
        print("Invalid unit")

temperature_converter()
