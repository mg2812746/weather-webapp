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