FROM nginx
RUN apt-get update \
    && apt-get install -y nginx-module-stub-status
COPY nginx.conf /etc/nginx/nginx.conf