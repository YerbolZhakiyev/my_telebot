FROM nginx:latest

RUN apt-get update && apt-get install -y

COPY /root/my_telebot/html /html
COPY /root/my_telebot/nginx/nginx.conf /etc/nginx/nginx.conf