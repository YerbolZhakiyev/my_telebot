import requests
import json
import logging


def test_get_1():
    logging.info('Starting test_get_1...')    
    response = requests.get('http://backend:8000/orders')
    json_obj = response.json()
    orders_array = json_obj['data']
    logging.info('Orders array: %s', orders_array)
    assert response.status_code == 200, 'Response status Test 1 ERROR'
    assert orders_array[0]['description'] == 'Test description', 'Test 1 ERROR'
    assert orders_array[1]['from_address'] == 'New York', 'Test 1 ERROR'

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    test_get_1()