FROM python:3.10-slim

ARG GITHUB_TOKEN
ENV GITHUB_TOKEN=${GITHUB_TOKEN}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV CXXFLAGS='-std=c++11'
ENV PARLANT_HOME=/app/data

WORKDIR /app

ENV POETRY_VERSION=1.8.3
RUN pip install poetry==$POETRY_VERSION
RUN apt-get update && apt-get install -y g++ git && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml /app/
COPY config /app/config

# ここでpyproject.tomlの${GITHUB_TOKEN}を実際の値に置換
RUN sed -i "s|\${GITHUB_TOKEN}|${GITHUB_TOKEN}|g" /app/pyproject.toml

RUN poetry config virtualenvs.create false && poetry install --only main

EXPOSE 8800
CMD ["poetry", "run", "parlant-server", "run", "--azure"]