
#api key: df7eb188d4f6b48e7b57de0fb03ba3ac

import requests
import datetime

api_key = input("Enter API key: ")
city_name = input("Enter city name: ")

url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
response = requests.get(url)
data = response.json()

# Example: Print temperature and weather description
if response.status_code == 200:
    print("Request successful!")
    print(f"datetime: {datetime.datetime.fromtimestamp(data['dt'])}")
    print(f"main: {data['main']}")
    print(f"weather: {data['weather']}")
    print(f"clouds: {data['clouds']}")
    print(f"wind: {data['wind']}")
else:
    print(f"Error: {response.status_code}")