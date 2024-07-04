'''
File: weather_api.py

Author: Miguel Galvez

Summary: 
    - Instantiates a WeatherAPI object with US city and state. 
    - Calling get_forecast_hourly() creates a json file with appropriate timestamp of relevant weather data of city and state.

Notes: 
    - Data is sourced from weather.gov API
'''
# modules
import os.path
import requests
import json
from datetime import date
from geopy.geocoders import Nominatim

# WeatherAPI Class - gets weather data
class WeatherAPI:
    def __init__(self, city: str , state: str):
        self.city = city
        self.state = state
        self.file = f'data/data_{self.city}_{self.state}_{date.today()}.json'

    # return city and state used to initiatize object
    def __str__(self):
        return f"Weather API object with city: {self.city} and state: {self.state}."

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
        # if forecast already found previously, merely throw already found message
        if os.path.isfile(self.file):
            print("weather data already found")
            return None
        geojson = self.get_geojson()
        gridpoints = self.get_gridpoints(geojson)
        forecast_json = requests.get(f"https://api.weather.gov/gridpoints/SGX/{str(gridpoints[0])},{str(gridpoints[1])}/forecast")
        forecast_json = forecast_json.json()
        self.export(f'{self.file}', forecast_json)
    
    # export text to file
    def export(self, file: str, data: dict) -> None:
        with open(f'{file}', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # import text from file
    def get_data_from_json(self, file: str) -> dict:
        with open(f'{file}') as fh:
            a = json.load(fh)
            # test
            # periods = a['properties']['periods']
            # print(periods)
        fh.close()
        return a

