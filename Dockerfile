FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

WORKDIR /code

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .