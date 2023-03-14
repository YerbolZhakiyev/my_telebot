FROM python:3.9
WORKDIR /tg_bot
COPY requirements.txt .
COPY /root/my_telebot/tg_bot/.env .env
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "./main.py" ]