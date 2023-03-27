FROM postgres

ENV POSTGRES_USER erbol
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB tg_bot
COPY ./01-schema.sql:/docker-entrypoint-initdb.d/01-schema.sql