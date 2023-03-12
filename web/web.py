import requests
import json

r = requests.get('http://web')
print(r.json())