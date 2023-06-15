import requests
import key
import json
city = str(input('Type the name of the city: '))
url = f'http://api.weatherapi.com/v1/current.json?key={key.api_key}&q={city}'

response = requests.get(url)
data = json.loads(response.text)

if response.status_code == 200:
  print('\nCity: {} - {}'.format(data['location']['name'], data['location']['country']))
  print('Weather: {}°C'.format(data['current']['temp_c']))
  print('Condition: {}'.format(data['current']['condition']['text']))
  print('Wind/km: {} km/h'.format(data['current']['wind_kph']))
  print('Humidity: {}%'.format(data['current']['humidity']))
  print('Thermal sensation: {}°C'.format(data['current']['feelslike_c']))
else:
  print("Python couldn't call the API")
