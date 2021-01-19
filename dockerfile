FROM python:3.8.6-buster as base

RUN pip install poetry
WORKDIR /project
COPY /todo_app /project/todo_app
COPY /tests/ /project/tests/
COPY  poetry.lock *.toml /project/
RUN cd /project/
RUN poetry install

FROM base as production
COPY docker-entrypoint.sh ./
CMD ["./docker-entrypoint.sh"]

FROM base as developments
COPY docker-flask-entrypoint.sh ./
CMD ["./docker-flask-entrypoint.sh"]