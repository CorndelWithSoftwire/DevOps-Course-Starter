#Using Python as base image
FROM python:3.8-slim-buster as base

#Installing dependencies
RUN apt-get update && apt-get install -y curl

WORKDIR /app
COPY . .

ENV APP_INSTALL=/app
ENV POETRY_HOME=/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}
ENV PYTHONPATH=${APP_INSTALL}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

RUN poetry config virtualenvs.create false --local && \\
    poetry install --no-dev --no-root



ENTRYPOINT ["poetry", "run", "flask", "run"]


