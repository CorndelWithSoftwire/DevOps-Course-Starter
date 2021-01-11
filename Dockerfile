# Perform common operations, dependency installation etc...
FROM python:3.9.0-buster as base
RUN pip install poetry
WORKDIR /DevOps-Course-Starter
COPY pyproject.toml /DevOps-Course-Starter/
COPY . /DevOps-Course-Starter/

# Configure for production
FROM base as production
RUN poetry install  --no-dev
ENTRYPOINT poetry run gunicorn "app:create_app()" --bind 0.0.0.0:5000

# Configure for local development
FROM base as development
RUN poetry install
ENTRYPOINT poetry run flask run -h 0.0.0.0 -p 5000