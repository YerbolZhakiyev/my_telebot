from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
BACKEND_HOST = os.getenv('backend_host')
response = requests.get(BACKEND_HOST + '/test')
if response.status_code == 200:
    assert False, "Error"
else:
    print('Flask is working without any issues')
