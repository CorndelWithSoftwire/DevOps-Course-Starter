FROM python:3.8 as base

# Get poetry and set PATH

ENV POETRY_HOME=/poetry       
ENV PATH=${POETRY_HOME}/bin:${PATH}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Get application files required and place in correct subdirectories
WORKDIR /app
RUN mkdir ./models
RUN mkdir ./templates
COPY ./app.py ./app.py 
COPY ./todo.py ./todo.py
COPY ./models/view_model.py ./models/view_model.py
COPY ./templates/layout.html ./templates/layout.html
COPY ./templates/index.html ./templates/index.html
COPY ./poetry.toml ./poetry.toml
COPY ./pyproject.toml ./pyproject.toml
COPY ./wsgi.py ./wsgi.py

#Install Poetry

RUN poetry install

#Entrypoints

#Production Gunicorn
FROM base as production

ENTRYPOINT poetry run gunicorn --bind 0.0.0.0:5000 wsgi:app

#Development Flask

FROM base as development

ENTRYPOINT poetry run flask run --host=0.0.0.0
