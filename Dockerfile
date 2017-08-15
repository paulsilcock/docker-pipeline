FROM python:alpine3.6

WORKDIR /data/app

ENV PYTHONPATH /data/app:$PYTHONPATH
ENV PATH /data/app/env/bin:$PATH

COPY requirements.txt requirements.txt

RUN python -m venv env
RUN . env/bin/activate && pip install -r requirements.txt

COPY demo demo
