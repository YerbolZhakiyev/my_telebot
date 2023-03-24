FROM nginx
RUN apt-get update \
    && apt-get install -y nginx-module-stub-status \
    && apt-get install -y --no-install-recommends curl
COPY nginx.conf /etc/nginx/nginx.conf
