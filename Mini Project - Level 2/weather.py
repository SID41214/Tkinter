# Description: A weather application that fetches data from an API (like OpenWeatherMap) and displays it.

# Features:

# Input city name.
# Fetch weather data using an API.
# Display temperature, humidity, and weather conditions.

import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    if city:
        api_key = "your_api_key"  # Replace with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric" 
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            result = f"Weather: {weather}\nTemperature: {temp}°C\nHumidity: {humidity}%"
        else:
            result = "City not found!"
        result_label.config(text=result)
    else:
        result_label.config(text="Please enter a city name!")

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather", command=get_weather)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
