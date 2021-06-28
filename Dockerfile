FROM python:3.8.5

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

WORKDIR /code

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .