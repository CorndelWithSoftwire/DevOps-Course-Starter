FROM python:3.7.9-slim-buster as base

ENV PATH /usr/local/bin:$PATH
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
WORKDIR /app
RUN pip install poetry
EXPOSE 5000
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-root
COPY . /app

FROM base as production
ENTRYPOINT poetry run gunicorn -w 4 -b 0.0.0.0:5000 run:app

FROM base as development
ENTRYPOINT poetry run flask run --host=0.0.0.0