import requests
import time

def get_data(apiNumber):
    if apiNumber == 0:
        response = requests.get('https://covid19-api.org/api/status')
    elif apiNumber == 1:
        response = requests.get('https://ridb.recreation.gov/api/v1/tours', params={'Authorization': 'Bearer b5677a68-ed4b-4781-befa-b04790fd5796'})
    else:
        response = {'status': 'invalid apiNumber'}
    return response