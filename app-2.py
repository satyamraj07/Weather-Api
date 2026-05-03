import requests
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("api_key")

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


response = requests.get(url)
data = response.json()


if data.get("cod") != 200:
    print("Error:", data.get("message"))
else:
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])


def configure():
    load_dotenv()
    
    
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return celsius, fahrenheit                                                  

kelvin_temp = data["main"]["temp"] + 273.15
celsius_temp, fahrenheit_temp = kelvin_to_celsius_fahrenheit(kelvin_temp)
temp_celsius = data["main"]["temp"]
temp_fahrenheit = temp_celsius * 9/5 + 32
feels_like_celsius = data["main"]["feels_like"]
feels_like_fahrenheit = feels_like_celsius * 9/5 + 32
temp_min_celsius = data["main"]["temp_min"]
temp_min_fahrenheit = temp_min_celsius * 9/5 + 32
temp_max_celsius = data["main"]["temp_max"]
temp_max_fahrenheit = temp_max_celsius * 9/5 + 32
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
description = data["weather"][0]["description"]
sunrise_time = data["sys"]["sunrise"]
sunset_time = data["sys"]["sunset"]
print(f"Temperature in Celsius: {celsius_temp:.2f} °C")
print(f"Temperature in Fahrenheit: {fahrenheit_temp:.2f} °F")   
print(f"Temperature in {city}: {temp_celsius: .2f}°C or {temp_fahrenheit}°F") 
print(f"Temperature in {city} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F") 
print(f"Minimum Temperature in {city}: {temp_min_celsius:.2f}°C or {temp_min_fahrenheit:.2f}°F") 
print(f"Maximum Temperature in {city}: {temp_max_celsius:.2f}°C or {temp_max_fahrenheit:.2f}°F")
print(f"Humidity in {city}: {humidity}%")
print(f"Wind Speed in {city}: {wind_speed}m/s")
print(f"General Weather in {city}: {description}")
print(f"Sun rises in {city} at {sunrise_time} local time.")
print(f"Sun sets in {city} at {sunset_time} local time.")