import requests
import json

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
    def get_geocoordinates(self) -> list:
        INDEX1 = '<div class="b_focusTextLarge">'
        INDEX2 = '</a>'
        HEADERS = {'Content-Type': 'text/html'}
        URL = f'https://www.bing.com/search?pglt=161&q={self.city}+{self.state}+latitude+longitude'
        coords = []

        r = requests.get(URL, HEADERS)
        text = r.text

        file_out = open("search_test.txt", "w")
        file_out.write(text)
        file_out.close()


        # find indexes of latitude and longitude
        #first = text.find(INDEX1)
        #last = text.find(INDEX2, first)

        #text = text[first:last]
        #print('first: '+ str(first) + ' last: ' + str(last))
        #print(text)
        
        return coords
    
# driver
testAPI = WeatherAPI('Fontana', 'California')
testAPI.get_geocoordinates()