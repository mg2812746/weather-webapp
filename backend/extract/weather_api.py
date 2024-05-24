import requests
import json
from geopy.geocoders import Nominatim

class WeatherAPI:
    def __init__(self, city: str , state: str):
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.city} {self.state}"
    # return latitude, longitude from city and state
    def geocode(self) -> list:
        geolocator = Nominatim(user_agent="weather visualizer")
        g = geolocator.geocode(f'{self.city}, {self.state}')
        coords = [g.latitude, g.longitude]
        return coords
    # to be completed
    def get_weather_data(self) -> json:
        coords = self.geocode()
        r = requests.get(f"https://api.weather.gov/points/{coords[0]},{coords[1]}")
        # Add timestamp of data accessed
        data = r.json()
        return data
    
    
# driver
testAPI = WeatherAPI('Fontana', 'CA')
data = testAPI.get_weather_data()
print(data)