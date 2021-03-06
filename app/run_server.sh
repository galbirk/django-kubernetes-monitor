#!/usr/bin/env bash
# start django server
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; 
then
    python manage.py collectstatic --noinput
fi
gunicorn --bind :8000 --workers 3 monitor_k8s.wsgi
