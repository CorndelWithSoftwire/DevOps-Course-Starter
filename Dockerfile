FROM python:3.8-slim-buster as base
RUN pip install poetry
EXPOSE 5000
WORKDIR /code
COPY ./todo_app /code/todo_app
COPY ./poetry.toml /code/
COPY ./pyproject.toml /code/

RUN poetry install
FROM base as dev
COPY ./pyproject.toml ./
RUN poetry install
COPY ./todo_app /code/
#ENTRYPOINT poetry run flask run -h 0.0.0.0 -p 5000
ENTRYPOINT ["poetry", "run", "flask run -h 0.0.0.0 -p 5000"]

################## prod ####################
FROM base as prod
WORKDIR /code
ENV PORT=5000
COPY pyproject.toml .
RUN poetry install
COPY ./todo_app /code/
RUN chmod 777 run.sh
ENV FLASK_ENV=production
ENTRYPOINT ./run.sh

FROM base as test
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
 apt-get install ./chrome.deb -y &&\
 rm ./chrome.deb
# Install Chromium WebDriver
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
 echo "Installing chromium webdriver version ${LATEST}" &&\
 curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
 apt-get install unzip -y &&\
 unzip ./chromedriver_linux64.zip
# Copy all files
COPY ./todo_app /code/todo_app
COPY ./poetry.toml /code/
COPY ./pyproject.toml /code/
#COPY ./.env /code/.env

# Setup the entry point
ENTRYPOINT ["poetry", "run", "pytest"]