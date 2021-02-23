FROM python:3.8.6-slim-buster as base


RUN pip install poetry
WORKDIR /project

FROM base as production
COPY  poetry.lock pyproject.toml /project/
COPY docker-entrypoint.sh ./
RUN cd /project/
RUN poetry install --no-dev
CMD ["./docker-entrypoint.sh"]

FROM base as developments
COPY /tests/ /project/tests/
COPY  poetry.lock pyproject.toml /project/
COPY docker-flask-entrypoint.sh ./docker-entrypoint.sh
RUN cd /project/
RUN poetry install
CMD ["./docker-entrypoint.sh"]