import requests
import json

r = requests.get('http://app:8000')
print(r.json())