#!/usr/bin/env bash

python leasing-king-api/app/manage.py migrate || { echo 'migration has been failted' ; exit 1; }

python leasing-king-api/app/manage.py collectstatic --noinput || { echo 'collectstatic has been failted' ; exit 1; }


# Gunicorn relies on the operating system to provide all of the load balancing when handling requests.
# Generally we recommend (2 x $num_cores) + 1 as the number of workers to start off with.
# While not overly scientific, the formula is based on the assumption that for a given core,
# one worker will be reading or writing from the socket while the other worker is processing a request.
cd leasing-king-api/app && gunicorn --workers 5 --bind 0.0.0.0:8000 -m 007 config.wsgi:application
