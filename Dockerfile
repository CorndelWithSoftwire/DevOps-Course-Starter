FROM python:3.8.6-buster as base
RUN pip install poetry
EXPOSE 5000
WORKDIR /code
COPY . /code/
RUN poetry install --no-root --no-dev
FROM base as dev
ENTRYPOINT poetry run flask run -h 0.0.0.0 -p 5000
FROM base as prod
ENV FLASK_ENV=production
ENTRYPOINT poetry run gunicorn "app:create_app()" --bind 0.0.0.0:5000