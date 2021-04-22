import requests
from pprint import pprint

API_Key = '3c35fadf3204409369a1ccce485cabfc'

city = input("Enter a city name!")
base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid={" + API_Key + "}"

weather_data = requests.get(base_url).json()

pprint(weather_data)

