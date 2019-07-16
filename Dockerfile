FROM python:3.7-alpine
LABEL maintener gcs

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update build-base \
    jpeg-dev \
    zlib-dev
RUN pip install -r /requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./src /src

RUN adduser -D gian
USER gian

