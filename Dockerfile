FROM 3.10.13-alpine3.18
LABEL authors="IslamTambiev"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
RUN chmod 755 .
COPY . .
CMD python bot.py