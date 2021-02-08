FROM python:3.7 as base

RUN mkdir /app 
WORKDIR /app
COPY *.toml /app/

ENV APP_INSTALL=/app
ENV POETRY_HOME=/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# DEVELOPMENT
FROM base as development
ENV FLASK_ENV=development

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev    
    
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

# PRODUCTION
FROM base as production

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY runGunicorn.sh /app
COPY gunicorn_config.py /app
COPY todoapp /app/todoapp

RUN chmod 755 runGunicorn.sh && \
    mkdir -p /var/log/gunicorn

ENV FLASK_ENV=production

ENTRYPOINT ["./runGunicorn.sh"]

# RUN TESTS
FROM base as unittests

ENV FLASK_ENV=development \
    PYTHONPATH=/app

RUN poetry config virtualenvs.create false && \
    poetry install

COPY todoapp /app/todoapp
COPY tests /app/tests

ENTRYPOINT ["poetry", "run", "pytest", "tests/unit", "--junit-xml", "test_results.xml"]

# RUN TESTS
FROM base as integrationtests

ENV FLASK_ENV=development \
    PYTHONPATH=/app

RUN poetry config virtualenvs.create false && \
    poetry install

COPY todoapp /app/todoapp
COPY tests /app/tests

ENTRYPOINT ["poetry", "run", "pytest", "tests/integration", "--junit-xml", "test_results.xml"]


# RUN TESTS
FROM base as endtoendtests

RUN apt-get update && apt-get install -y \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    xvfb

# install geckodriver and firefox

RUN GECKODRIVER_VERSION=`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'` && \
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz && \
    tar -zxf geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz

RUN FIREFOX_SETUP=firefox-setup.tar.bz2 && \
    wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-latest&os=linux64" && \
    tar xjf $FIREFOX_SETUP -C /opt/ && \
    ln -s /opt/firefox/firefox /usr/bin/firefox && \
    rm $FIREFOX_SETUP

ENV FLASK_ENV=development \
    PYTHONPATH=/app

RUN poetry config virtualenvs.create false && \
    poetry install
    
COPY todoapp /app/todoapp
COPY tests /app/tests

ENTRYPOINT ["poetry", "run", "pytest", "tests/endtoend", "--junit-xml", "test_results.xml"]



