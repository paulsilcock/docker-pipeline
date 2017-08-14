FROM python:3.6

WORKDIR /data/demo

COPY requirements.txt requirements.txt

RUN python -m venv /data/demo/env && . /data/demo/env/bin/activate
RUN pip install -r requirements.txt
