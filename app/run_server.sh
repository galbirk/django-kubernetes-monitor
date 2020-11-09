#!/usr/bin/env bash
# start django server
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; 
then
    python manage.py collectstatic
		python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser --no-input
fi
gunicorn --bind :8000 --workers 3 monitor_k8s.wsgi
