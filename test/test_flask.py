import requests
from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
BACKEND_HOST = os.getenv('backend_host')
response = requests.get('http://' + BACKEND_HOST + ':8000/orderss')
if response.status_code == 200:
    print('Flask is working without any issues')
else:
    assert False, "Error"