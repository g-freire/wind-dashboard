FROM python:3.6.3-alpine3.6@sha256:aba3798848cd840e9d06f04e1dca81c82677e72e69ad9b2240a46c6754e56eab as base

ENV TERM xterm
RUN apk add --no-cache --virtual build-dependencies make gcc \
    g++ libxml2-dev libxslt-dev libffi-dev python3-dev

WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

# CMD gunicorn server:app -k gevent --worker-connections 1000
# CMD gunicorn -c gunicorn/dev_config.py wsgi:app 

EXPOSE 5001  

# ENTRYPOINT ["python3","server.py"]   # to run flask server in dev mode call app.run in server.py

# sometimes you need to restart docker using win10/64x
# error starting userland proxy .. input/output