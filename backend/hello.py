from flask import Flask, request, render_template
from extract.weather_api import WeatherAPI

app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read-form', methods=['POST'])
def read_form():

    # Get form data as dict
    data = request.form

    # Demonstration of ETL Process (Extract, Transform, Load)
    # Extract Data 

    w = WeatherAPI(data['city'], data['state'])
    
    w.get_forecast_hourly()
    
    # Transform JSON into usable data to be displayed to webapp

    try:
        a = w.get_data_from_json()
        l_data = a['properties']['periods']
        # Get appropriate data from each element and write to file
        weather = dict()
        
        for l in l_data:
            temp = l
            day = temp['name']
            temperature = temp['temperature'] # assume unit is Farenheit
            d_forecast = temp['detailedForecast']
            weather[day]=(f'{{{temperature} F, {d_forecast}}}')

        return weather
    except:
        print("Error: File doesn't exist! can't proceeed with data transformation")
        return {
            'response': 500,
            'error': "Could not find weather data file"
        }

if __name__ == '__main__':
    # Run the app on local development server
    app.run()