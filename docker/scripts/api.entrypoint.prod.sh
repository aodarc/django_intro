#!/usr/bin/env bash

python leasing-king-api/app/manage.py migrate || { echo 'migration has been failted' ; exit 1; }

python leasing-king-api/app/manage.py collectstatic --noinput || { echo 'collectstatic has been failted' ; exit 1; }

cd leasing-king-api/app && gunicorn --workers 4 --bind 0.0.0.0:8000 -m 007 config.wsgi:application
