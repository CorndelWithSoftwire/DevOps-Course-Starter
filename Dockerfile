FROM python:3.8.6-slim-buster as base

RUN apt-get update \
    && apt-get install -y curl \
    && mkdir todo_app \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python 
RUN ["/bin/bash", "-c", "source /root/.poetry/env"]
ENV PATH="${PATH}:/root/.poetry/bin"
WORKDIR /todo_app
COPY todo_app/poetry.toml todo_app/pyproject.toml ./
RUN poetry install

FROM base as production
EXPOSE 5000
COPY todo_app todo_app
ENTRYPOINT [ "poetry", "run", "gunicorn", "--config", "gunicorn.conf.py", "app:create_app()" ]

FROM base as development
EXPOSE 5000
ENTRYPOINT [ "poetry", "run", "flask", "run", "--host", "0.0.0.0"]