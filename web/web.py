import requests
import json

r = requests.get('http://app')
print(r.json())