FROM python:3.10.12-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev

COPY requirements/base.txt base.txt
COPY requirements/production.txt production.txt

RUN pip install pip --upgrade  && pip install -r production.txt

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media

WORKDIR $APP_HOME

COPY . .

RUN ["chmod", "+x", "/home/app/web/entrypoint.sh"]

RUN rm -rf /etc/apk/cache