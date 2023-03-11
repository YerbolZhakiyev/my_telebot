FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY /root/my_telebot/nginx/nginx.conf /etc/nginx/conf.d
RUN mkdir -p /home/web/default