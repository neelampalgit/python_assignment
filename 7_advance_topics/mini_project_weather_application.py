import requests

def weather_application():
    city = input("Enter city name: ")
    api_key = "your_api_key_here"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] == "404":
        print("City not found.")
    else:
        main = data["main"]
        temperature = main["temp"] - 273.15  # Convert from Kelvin to Celsius
        weather = data["weather"][0]["description"]
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature:.2f}°C")

weather_application()
