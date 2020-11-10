#!/bin/bash
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; 
then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser --no-input
fi