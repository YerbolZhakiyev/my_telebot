FROM python:3.9

WORKDIR /root/my_telebot/app
COPY requirements.txt /root/my_telebot/app
RUN apt pip3 install --upgrade pip && apt pip3 install -r requirements.txt

EXPOSE 5000

COPY . /root/my_telebot/app