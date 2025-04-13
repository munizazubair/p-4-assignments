import requests
from pprint import pprint

API_KEY = "931551918dede09001c2a15e8581b111"
city = input("Enter the city name: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q=" + city
weather_data = requests.get(base_url).json()
pprint(weather_data)