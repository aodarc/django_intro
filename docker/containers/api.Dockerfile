FROM python:3.8-slim

ADD . /django_intro

RUN chmod +x /django_intro/docker/scripts/api.entrypoint.dev.sh && \
    chmod +x /django_intro/docker/scripts/wait-for-it.sh

RUN apt-get update && apt-get install -y gettext \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /django_intro/requirements/dev.txt
