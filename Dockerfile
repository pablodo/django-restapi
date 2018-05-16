FROM python:3.6

MAINTAINER Pablo Diaz Ogni <pablo.diazogni@gmail.com>

RUN apt-get update && \
    pip install -U setuptools pip

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

