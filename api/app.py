import requests
from flask import Flask, jsonify, request
from service import get_ip, get_temperature



app = Flask(__name__)




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