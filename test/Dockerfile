FROM python:3.9
COPY requirements.txt .
COPY tests.py tests.py
RUN pip install requests
CMD [ "python3", "tests.py" ]