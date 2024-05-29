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
    # get grid endpoints
    def get_gridpoints(self, geojson: dict) -> list:
        gridpoints = [geojson['properties']['gridX'], geojson['properties']['gridY']]
        return gridpoints
    # get geojson from latitude and longitude
    def get_geojson(self) -> str:
        coords = self.geocode()
        r = requests.get(f"https://api.weather.gov/points/{coords[0]},{coords[1]}")
        # Add timestamp of data accessed
        data = r.json()
        return data
    # get hourly forcast data
    def get_forecast_hourly(self) -> None:
        geojson = self.get_geojson()
        gridpoints = self.get_gridpoints(geojson)
        forecast_json = requests.get(f"https://api.weather.gov/gridpoints/SGX/{str(gridpoints[0])},{str(gridpoints[1])}/forecast")
        forecast_json = forecast_json.json()
        # forecast_json = eval(forecast_json)
        # data = self.get_data_from_json('data.json')
    # export text to file
    def export(self, file: str, data: dict) -> None:
        with open(f'{file}', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    # import text from file
    def get_data_from_json(self, file: str) -> dict:
        with open(f'{file}') as fh:
            a = json.load(fh)
        fh.close()
        return a
# driver
testAPI = WeatherAPI('Fontana', 'CA')
testAPI.get_forecast_hourly()
