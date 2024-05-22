import requests
import json

class WeatherAPI:
    def __init__(self, city: str , state: str):
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.city} {self.state}"
    # to be completed
    def get_weather_data(city : str, state: str) -> json:
        data = {}
        data = json.dumps(data)

        return data
    # return latitude, longitude from city and state
    def get_geocoordinates(city: str, state: str) -> list:
        INDEX1 = '<div class="b_focusTextLarge">'
        INDEX2 = '</div>'
        coords = []
        r = requests.get(f'https://www.bing.com/search?pglt=161&q={city}+{state}+latitude+longitude')
        text = r.text
        
        
        return coords