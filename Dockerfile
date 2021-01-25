FROM python:3.8 as base

# Get poetry and set PATH

ENV POETRY_HOME=/poetry       
ENV PATH=${POETRY_HOME}/bin:${PATH}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Get application files required and place in correct subdirectories
WORKDIR /app
RUN mkdir ./models
RUN mkdir ./templates
COPY ./todo_app/app.py ./todo_app/app.py 
COPY ./todo_app/todo.py ./todo_app/todo.py
COPY ./todo_app/models/view_model.py ./todo_app/models/view_model.py
COPY ./todo_app/templates/layout.html ./todo_app/templates/layout.html
COPY ./todo_app/templates/index.html ./todo_app/templates/index.html
COPY ./poetry.toml ./poetry.toml
COPY ./pyproject.toml ./pyproject.toml
COPY ./todo_app/wsgi.py ./todo_app/wsgi.py

#Install Poetry

RUN poetry install

#Entrypoints

#Production Gunicorn
FROM base as production

ENTRYPOINT poetry run gunicorn --bind 0.0.0.0:5000 todo_app.wsgi:app

#Development Flask

FROM base as development

ENTRYPOINT poetry run flask run --host=0.0.0.0

#Test
FROM base as test

ENTRYPOINT ["poetry", "run", "pytest"]