import requests
from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
BACKEND_HOST = os.getenv('backend_host')
response = requests.get(BACKEND_HOST + '/test_orders')
json_obj = response.json()
orders_array = json_obj['data']
if response.status_code == 200:
    print(orders_array)
    print('Flask is working without any issues')
else:
    assert False, "Error"