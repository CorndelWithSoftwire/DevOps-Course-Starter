FROM python:3.8 as base

# Get poetry and set PATH

ENV POETRY_HOME=/poetry       
ENV PATH=${POETRY_HOME}/bin:${PATH}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

RUN apt-get update
# Install Chrome
 RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
 	apt-get install ./chrome.deb -y &&\
	rm ./chrome.deb
  
  
# Install Chromium WebDriver

RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\ 
    echo "Installing chromium webdriver version ${LATEST}" &&\
 	curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
 	apt-get install unzip -y &&\
 	unzip ./chromedriver_linux64.zip

# Selenium Setup 



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
COPY ./todo_app/test_unit.py ./todo_app/test_unit.py
COPY ./todo_app/test_integration.py ./todo_app/test_integration.py
COPY ./todo_app/test_e2e.py ./todo_app/test_e2e.py




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