FROM python:2.7-onbuild
RUN apt-get update

RUN apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev python-psycopg2 libpq-dev libxslt1-dev zlib1g-dev python-ldap nodejs npm

ENV PYTHONUNBUFFERED 1