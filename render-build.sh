#!/usr/bin/env bash
python manage.py migrate --noinput
gunicorn core.wsgi:application --bind 0.0.0.0:8000
