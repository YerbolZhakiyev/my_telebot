FROM python:3.9-slim-buster
WORKDIR my_telebot/app
COPY requirements.txt requirements.txt
COPY /root/my_telebot/app/data.json data.json
RUN pip3 install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "web:app"]