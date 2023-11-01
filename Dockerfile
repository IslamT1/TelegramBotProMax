FROM 3.10.13-alpine3.18
LABEL authors="IslamTambiev"
COPY . .
RUN pip3 install -r requirements.txt
CMD python bot.py