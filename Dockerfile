FROM python:3.8.6-slim-buster

RUN apt-get update &&\
    apt-get install -y curl &&\
    mkdir todo_app &&\
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python 
RUN ["/bin/bash", "-c", "source /root/.poetry/env"]
ENV PATH="${PATH}:/root/.poetry/bin"
COPY todo_app todo_app
WORKDIR /todo_app
RUN poetry install
EXPOSE 5000
ENTRYPOINT [ "poetry", "run", "gunicorn", "--config", "gunicorn.conf.py", "app:create_app()" ]