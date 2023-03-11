FROM python:3.9

WORKDIR /root/my_telebot/app
COPY requirements.txt /root/my_telebot/app
RUN pip install --upgrade pip && -m pip install -r requirements.txt

EXPOSE 5000

COPY . /root/my_telebot/app