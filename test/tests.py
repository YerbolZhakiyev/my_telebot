import requests
import json

def test_get_1():
    response = requests.get('test_backend/orders')
    json_obj = response.json()
    orders_array = json_obj['data']
    assert response.status_code == 200, 'Response status Test 1 ERROR'
    assert orders_array[0][0] == 'Test description', 'Test 1 ERROR'
    assert orders_array[1][1] == 'New York', 'Test 1 ERROR'

def test_get_2():
    response = requests.get('test_backend/orders')
    json_obj = response.json()
    orders_array = json_obj['data']
    assert response.status_code == 200, 'Response status Test 2 ERROR'
    assert orders_array[0][0] == 'ABCD', 'Test 2 ERROR'
    assert orders_array[1][1] == 'ABCD', 'Test 2 ERROR'

def test_post():
    name = 'John Smith'
    id = 123
    json_data = json.dumps({'name': name, 'tg_id': id})
    headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post('test_backend/customers', data=json_data, headers=headers)
    assert response.status_code == 200, 'Response status Test 3 ERROR'

test_get_1()
test_get_2()
test_post()