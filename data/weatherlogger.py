import requests
import json
from datetime import datetime, timezone
import time

api_key = '411643adb85919a3e30478e6ada681f4'
filename = '/home/jendsen/WeatherLogger/weatherdata.json'
latlon1 = [39.112174, -77.146891]
latlon2 = [33.782384, -84.399855]
latlon3 = [29.418609, -98.481866]
latlon4 = [27.066850, -82.219010]
latlon5 = [34.729928, -86.587878]
latlonlist = [latlon1, latlon2, latlon3, latlon4, latlon5]

for latlon in latlonlist:
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + str(latlon[0]) + '&lon=' + str(latlon[1]) + '&appid=' + api_key
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())  # Parse JSON response
        utc_time = datetime.now(timezone.utc)
        temp = response.json()
        new_data = {'utc_time': str(utc_time)}
        temp.update(new_data)
        with open(filename, 'a') as f:
            f.write(json.dumps(temp) + "\n")
    time.sleep(5)
