from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
BACKEND_HOST = os.getenv('backend_host')
name = 'John Smith'
id = 123
json_data = json.dumps({'name': name, 'tg_id': id})
headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(BACKEND_HOST + '/test_customers', data=json_data, headers=headers)
if response.status_code == 200:
    print('Flask is working without any issues')
else:
    assert False, "Error"
