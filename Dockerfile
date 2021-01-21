# Perform common operations, dependency installation etc...
FROM python:3.9.0-buster as base
RUN pip install poetry
WORKDIR /DevOps-Course-Starter
COPY pyproject.toml /DevOps-Course-Starter/
COPY . /DevOps-Course-Starter/

# Configure for production
FROM base as production
RUN poetry install  --no-dev
ENTRYPOINT poetry run gunicorn "app:create_app()" --bind 0.0.0.0:5000

# Configure for local development
FROM base as development
RUN poetry install
ENTRYPOINT poetry run flask run --host=0.0.0.0

# testing stage
FROM base as test
RUN poetry install
ENTRYPOINT ["poetry", "run", "pytest"]

# Install Chrome 
RUN apt-get update
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
    apt-get install ./chrome.deb -y &&\  
    rm ./chrome.deb 

# Install Chromium WebDriver 
RUN apt-get update
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d ./

ENTRYPOINT [ "poetry", "run", "pytest" ]