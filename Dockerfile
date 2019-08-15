FROM python:3

WORKDIR /code

ENV DB_NAME_OLTP=oltp
ENV DB_USER_OLTP=oltp
ENV DB_PASS_OLTP=oltp

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .





