FROM python:3.9

LABEL maintainer="Gal Birkman, Devops Engineer. galbirkman@gmail.com"

EXPOSE 8000

ENV DJANGO_SUPERUSER_USERNAME=galbirkman \
    DJANGO_SUPERUSER_PASSWORD=Aa123456 \
    DJANGO_SUPERUSER_EMAIL=mymail@gmail.com

WORKDIR /app

COPY . .

RUN chmod 755 run_server.sh && pip install -r requirements.txt

CMD ["/app/run_server.sh"]