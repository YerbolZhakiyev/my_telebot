FROM python:3.9-slim-buster
WORKDIR /test_backend
COPY requirements.txt requirements.txt
COPY .env .env
RUN pip3 install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "test_backend:app"]