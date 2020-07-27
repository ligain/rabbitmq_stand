FROM python:3.8

WORKDIR /app
COPY ./examples /app

RUN pip install celery pika
