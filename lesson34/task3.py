import requests


city = input('Choose city: ')
api_url = 'https://api.openweathermap.org/data/2.5/weather'
appid = 'a5cf108e68d4bf8baec4429fdd7d0e3a'
params = {'q': city, 'units': 'metric', 'appid': appid}

response = requests.get(api_url, params)
weather_data = response.json()

print(weather_data['main'])
