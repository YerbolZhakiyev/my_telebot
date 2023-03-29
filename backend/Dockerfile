FROM python:3.9-slim-buster
WORKDIR /backend
EXPOSE 8000
RUN apt-get update && apt-get install -y curl 
COPY requirements.txt requirements.txt
COPY .env .env
RUN pip3 install -r requirements.txt
COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "backend:app"]