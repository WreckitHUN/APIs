from flask import Flask, render_template, redirect, request
import requests
app = Flask(__name__)


red = {
    "red": 255,
    "green": 0,
    "blue": 0
}


green = {
    "red": 0,
    "green": 255,
    "blue": 0
}

blue = {
    "red": 0,
    "green": 0,
    "blue": 255
}

blank = {
    "red": 0,
    "green": 0,
    "blue": 0
}


@app.route('/data')
def get_data():
    response = requests.get('http://192.168.0.186/data')
    return response.json()


# Home page
@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')


url = 'http://192.168.0.186/led'


# Sending the colors
@app.route('/led', methods=["POST"])
def led():

    color = request.form['color']
    if color == "red":
        response = requests.post(url, json=red)
    if color == "green":
        try:
            response = requests.post(url, json=green)
        except:
            return redirect('/')
    if color == "blue":
        response = requests.put(url, json=blue)
    if color == "blank":
        response = requests.post(url, json=blank)
    print(color)
    if response.status_code == 200:
        print('JSON data sent successfully!')
    else:
        print('Failed to send JSON data:', response.status_code)
    return redirect('/')


if __name__ == '__main__':
    # Create the database when code is run
    # with app.app_context():
    # db.create_all()
    # Development mode
    app.run(host='127.0.0.1', port=8000, debug=True)
