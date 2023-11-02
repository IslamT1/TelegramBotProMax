FROM python:3.10-alpine
LABEL authors="IslamTambiev"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD python bot.py