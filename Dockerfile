#Using Python as base image
FROM python:3.8-slim-buster as base

ENV LIBRARY_PATH=/lib:/usr/lib
ENV APP_INSTALL=/app
ENV POETRY_HOME=/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}
ENV PYTHONPATH=${APP_INSTALL}

#Installing dependencies
RUN apt-get update && apt-get install -y curl

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

WORKDIR /app
COPY . .

RUN poetry config virtualenvs.create false --local && \\
poetry install --no-dev --no-root

ENTRYPOINT ["poetry", "run", "gunicorn", "todo-app.app:todo_app"]
CMD ["--bind", "0.0.0.0:80"]
EXPOSE 80

