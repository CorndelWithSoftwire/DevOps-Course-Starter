#Using Python as base image
FROM python:3.8-slim-buster as base


ENV LIBRARY_PATH=/lib:/usr/lib
ENV APP_INSTALL=/app
ENV POETRY_HOME=/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}
ENV PYTHONPATH=${APP_INSTALL}


#Installing dependencies
RUN apt-get update && apt-get install -y curl

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python


WORKDIR /app
COPY . .
RUN poetry config virtualenvs.create false --local && \
poetry install --no-dev --no-root


FROM base as production
# Configure for production
ENV FLASK_ENV=production
ENTRYPOINT ["poetry", "run", "gunicorn", "app:app"]
CMD ["--bind", "0.0.0.0:80"]
EXPOSE 80

FROM base as development
# Configure for local development
ENV FLASK_ENV=development
ENTRYPOINT ["poetry", "run", "flask", "run"]
CMD ["--host", "0.0.0.0"]
EXPOSE 5000


# testing stage

FROM base as test

# Installation required for selenium
RUN apt-get update -y \
    && apt-get install --no-install-recommends --no-install-suggests -y tzdata ca-certificates bzip2 curl wget libc-dev libxt6 \
    && apt-get install --no-install-recommends --no-install-suggests -y `apt-cache depends firefox-esr | awk '/Depends:/{print$2}'` \
    && update-ca-certificates \
    # Cleanup unnecessary stuff
    && apt-get purge -y --auto-remove \
    -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/* /tmp/*

# install geckodriver
RUN GECKODRIVER_VERSION=`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'` && \
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz && \
    tar -zxf geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz

# install firefox
RUN FIREFOX_SETUP=firefox-setup.tar.bz2 && \
    wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-latest&os=linux64" && \
    tar xjf $FIREFOX_SETUP -C /opt/ && \
    ln -s /opt/firefox/firefox /usr/bin/firefox && \
    rm $FIREFOX_SETUP




