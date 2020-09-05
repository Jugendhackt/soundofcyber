import requests
import os

def get_data(apiNumber):
    if apiNumber == 0:
        response = requests.get('https://covid19-api.org/api/status')
    else:
        response = {'status': 'invalid apiNumber'}
    return response