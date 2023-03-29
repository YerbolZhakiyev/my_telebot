import requests
import json

def test_get_1():
    response = requests.get('http://backend:8000/orders')
    json_obj = response.json()
    orders_array = json_obj['data']
    print(orders_array)
    assert response.status_code == 200, 'Response status Test 1 ERROR'
    assert orders_array[0]['description'] == 'Test description', 'Test 1 ERROR'
    assert orders_array[1]['from_address'] == 'New York', 'Test 1 ERROR'

def test_get_2():
    response = requests.get('http://backend:8000/orders')
    json_obj = response.json()
    orders_array = json_obj['data']
    assert response.status_code == 200, 'Response status Test 2 ERROR'
    assert orders_array[0]['description'] == 'ABCD', 'Test 2 success'
    assert orders_array[1]['from_address'] == 'ABCD', 'Test 2 success'

def test_post():
    name = 'John Smith'
    id = 123
    json_data = json.dumps({'name': name, 'tg_id': id})
    headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post('http://backend:8000/customers', data=json_data, headers=headers)
    assert response.status_code == 200, 'Response status Test 3 success'

test_get_1()
test_post()
test_get_2()