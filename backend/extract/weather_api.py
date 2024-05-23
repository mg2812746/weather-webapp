import requests
import json
from geopy.geocoders import Nominatim

class WeatherAPI:
    def __init__(self, city: str , state: str):
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.city} {self.state}"
    # to be completed
    def get_weather_data(self) -> json:
        data = {}
        data = json.dumps(data)
        
        return data
    # return latitude, longitude from city and state
    def geocode(self) -> list:
        geolocator = Nominatim(user_agent="weather visualizer")
        g = geolocator.geocode(f'{self.city}, {self.state}')
        coords = [g.latitude, g.longitude]
        return coords
    
# driver
testAPI = WeatherAPI('Fontana', 'CA')