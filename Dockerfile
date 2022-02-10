FROM python:3.9.9-alpine3.15

LABEL maintainer="Pham Manh Hung<phammanhhung109@gmail.com>"

# set work directory
WORKDIR /usr/src/app
# copy project
COPY ./server/web /usr/src/app/
# copy crontab
COPY crontab etc/cron.d/crontab
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt
    # chmod 0644 etc/cron.d/crontab

# CMD ["cron", "-f"]
CMD ["sh","-c","gunicorn --bind 0.0.0.0:8000 app:app"]