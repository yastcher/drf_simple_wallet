FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y python3-dev pkg-config default-libmysqlclient-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

COPY pyproject.toml .

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .
