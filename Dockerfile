FROM python:alpine3.6

WORKDIR /data/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY demo demo
