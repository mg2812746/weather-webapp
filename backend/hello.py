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

    ## Process the extracted data
    # city = data['city']
    # state = data['state']

    # Demonstration of ETL Process (Extract, Transform, Load)
    # Extract Data 
    w = WeatherAPI(data['city'], data['state'])

    w.get_forecast_hourly()
    return{
        'city': data['city'],
        'state': data['state'],
    }

if __name__ == '__main__':
    # Run the app on local development server
    app.run()