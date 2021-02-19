FROM python:3.8-slim-buster as base
RUN pip install poetry
EXPOSE 5000
WORKDIR /code

FROM base as dev
COPY ./pyproject.toml ./
RUN poetry install
COPY ./todo_app /code/
ENTRYPOINT poetry run flask run -h 0.0.0.0 -p 5000

FROM base as prod
COPY pyproject.toml .
RUN poetry install
COPY ./todo_app /code/
ENV FLASK_ENV=production
ENTRYPOINT poetry run gunicorn "todo_app.app:create_app()" --bind 0.0.0.0:5000

