FROM python:3.8-slim

RUN apt-get update && apt-get install -y gettext

ADD . /django_intro

RUN chmod +x /django_intro/docker/scripts/api.entrypoint.dev.sh && \
    chmod +x /django_intro/docker/scripts/wait-for-it.sh

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /django_intro/requirements/dev.txt
