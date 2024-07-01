import json
import requests
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

import requests

def get_ip():
    response = requests.get('https://ipinfo.io/json').json()
    ip = request.remote_addr
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()
    client_ip = response["ip"]
    city = response["city"]
    lat = response["latitude"]
    lon = response["longitude"]
    return client_ip, city, lat, lon


def get_temperature(lat, lon):
    temp_resp = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat}%2C%20{lon}?unitGroup=metric&key=XCN2PGTTQUNJHS3YALETAUUYA&contentType=json').json()
    return temp_resp['currentConditions']['temp']


@app.route('/api/hello', methods=["get"])
def hello():
    visitor_name = request.args.get('visitor_name')
    client_ip, city, lat, lon = get_ip()
    temperature = get_temperature(lat, lon)
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {city}"
    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    }

    formatted_response = json.dumps(response, indent=4)

    return Response(formatted_response, mimetype='application/json')


if __name__ == '__main__':
    app.run()


