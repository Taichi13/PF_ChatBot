FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV CXXFLAGS='-std=c++11'
ENV PARLANT_HOME=/app/data
ENV PYTHONPATH=/app

WORKDIR /app

ENV POETRY_VERSION=1.8.3
RUN pip install poetry==$POETRY_VERSION
RUN apt-get update && apt-get install -y g++ git && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml /app/
COPY config /app/config
COPY parlant /app/parlant

RUN poetry config virtualenvs.create false && poetry install --only main

EXPOSE 8800
CMD ["poetry", "run", "parlant-server", "run", "--azure"]