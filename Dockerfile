FROM python:3.8 as base

# Get poetry and set PATH

ENV POETRY_HOME=/poetry       
ENV PATH=${POETRY_HOME}/bin:${PATH}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# RUN sudo apt update
# Install Chrome
# RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
# 	apt-get install ./chrome.deb -y &&\
#	rm ./chrome.deb
#

# FROM debian:jessie
# ENV CHROME_VERSION "google-chrome-stable"
# RUN sed -i -- 's&deb http://deb.debian.org/debian jessie-updates main&#deb http://deb.debian.org/debian jessie-updates main&g' /etc/apt/sources.list \
#   && apt-get update && apt-get install wget -y
# ENV CHROME_VERSION "google-chrome-stable"
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#   && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list \
#   && apt-get update && apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable}
# CMD /bin/bash

# Install Chromium WebDriver

# RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\ 
#     echo "Installing chromium webdriver version ${LATEST}" &&\
# 	curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
# 	apt-get install unzip -y &&\
# 	unzip ./chromedriver_linux64.zip



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
# COPY ./todo_app/test_Todo.py ./todo_app/test_Todo.py
COPY ./todo_app/test_Newviewmodel.py ./todo_app/test_Newviewmodel.py



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