FROM python:3.11.1-slim-buster

RUN mkdir /app
WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY ./poetry.lock ./pyproject.toml /app/
RUN poetry install --no-dev
