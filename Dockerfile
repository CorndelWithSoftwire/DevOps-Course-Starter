FROM python:3.8.6-slim-buster

RUN apt-get update &&\
    apt-get install -y curl &&\
    mkdir todo_app &&\
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python 
RUN ["/bin/bash", "-c", "source /root/.poetry/env"]
ENV PATH="${PATH}:/root/.poetry/bin"
RUN mkdir tests_e2e && mkdir tests && mkdir templates
COPY flask_config.py viewmodel.py Trello_items.py Trello_boards.py README.md pyproject.toml poetry.toml poetry.lock gunicorn.conf.py app.py .env ./ 
COPY tests_e2e/ tests_e2e/ 
COPY tests/ tests/ 
COPY templates/ templates/
ENTRYPOINT [ "poetry", "run", "flask", "run"]