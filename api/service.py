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


