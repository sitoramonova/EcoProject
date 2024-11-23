FROM python:3.9

WORKDIR /code
COPY requirements.txt /code/

# Установка пакетов с указанием вывода ошибок для диагностики
RUN pip install -r requirements.txt || cat /code/requirements.txt
COPY . /code/