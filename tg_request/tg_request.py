import requests
import json

r = requests.get('http://backend:8000')
print(r.json())