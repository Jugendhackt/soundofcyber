import requests

def get_covid_data():
    response = requests.get('https://covid19-api.org/api/status')
    return response