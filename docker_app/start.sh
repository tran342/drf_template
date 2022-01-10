#!/bin/bash

python manage.py collectstatic --no-input --settings=conf.settings.local
python manage.py migrate --settings=conf.settings.local
gunicorn conf.wsgi:application --bind 0.0.0.0:8000 --workers 3
