FROM python:3.8.6-buster

RUN pip install poetry
WORKDIR /project
COPY /todo_app /project/todo_app
COPY /tests/ /project/tests/
COPY  poetry.lock *.toml .env.test /project/
RUN cd /project/
RUN poetry install
COPY docker-entrypoint.sh ./
CMD ["./docker-entrypoint.sh"]