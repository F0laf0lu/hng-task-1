import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

import requests

def get_ip():
    response = requests.get('https://ipinfo.io/json').json()
    client_ip = response["ip"]
    city = response["city"]
    lon, lat = response["loc"].split(",")
    return client_ip, city, lon, lat


def get_temperature(city):
    temp_resp = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&include=current&key=XCN2PGTTQUNJHS3YALETAUUYA&contentType=json').json()
    return temp_resp['currentConditions']['temp']


@app.route('/api/hello', methods=["get"])
def hello():
    visitor_name = request.args.get('visitor_name')
    client_ip, city, lon, lat = get_ip()
    temperature = get_temperature(city)
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {city}"
    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()