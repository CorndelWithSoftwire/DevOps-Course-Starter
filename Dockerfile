FROM python:3.9.6-slim-buster as base 

RUN apt-get update \
    && apt-get -y install curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

COPY . /app 
WORKDIR /app 
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry install 
EXPOSE 5000

FROM base as production
ENV FLASK_ENV=production
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:5000", "todo_app.app:create_app()"]

FROM base as development
CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]

FROM base as test
ENV PATH="${PATH}:/root/todo_app/tests"
CMD ["poetry", "run", "pytest"]
