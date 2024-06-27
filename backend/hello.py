from flask import Flask, request, render_template

app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read-form', methods=['POST'])
def read_form():

    # Get form data as dict
    data = request.form

    ## Return the extracted information
    return {
        'city': data['city'],
        'state': data['state'],
    }

if __name__ == '__main__':
    # Run the app on local development server
    app.run()