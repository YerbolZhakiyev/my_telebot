FROM python:3.9
WORKDIR /tg_bot
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "./main.py" ]