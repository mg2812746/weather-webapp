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
    try:
        w.get_forecast_hourly()
    except:
        print("Error getting forcast data")
    
    # Transform JSON into usable data to be displayed to webapp

    a = w.get_data_from_json()
    
    l_data = a['properties']['periods']

    l_data = list(l_data) 

    d_list = (dict(l) for l in l_data)

    print(d_list)

    return{
        'city': data['city'],
        'state': data['state'],
    }

if __name__ == '__main__':
    # Run the app on local development server
    app.run()