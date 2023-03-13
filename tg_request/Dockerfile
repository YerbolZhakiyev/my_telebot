FROM python:3.9-slim-buster
WORKDIR /tg_request
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "tg_request.py"]