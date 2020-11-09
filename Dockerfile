#Using Python as base image
FROM python:3.8-slim-buster as base

#Installing dependencies
RUN apt-get update && apt-get install -y curl




RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV POETRY_HOME=/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}

WORKDIR /todoapp
COPY . .



ENTRYPOINT ["./run.sh"]


