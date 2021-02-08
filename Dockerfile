FROM python:3.8.6-buster as base
RUN pip install poetry
EXPOSE 5000
WORKDIR /code
COPY ./todo_app /code/todo_app
COPY ./poetry.lock /code/
COPY ./poetry.toml /code/
COPY ./pyproject.toml /code/
RUN poetry install --no-root --no-dev
FROM base as dev
ENTRYPOINT poetry run flask run -h 0.0.0.0 -p 5000
FROM base as prod
ENV FLASK_ENV=production
ENTRYPOINT poetry run gunicorn "todo_app.app:create_app()" --bind 0.0.0.0:5000

FROM base as test
COPY ./pyproject.toml .
RUN poetry install


# Install the latest versions of Mozilla Firefox and Geckodriver
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests --assume-yes \
    curl \
    bzip2 \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    xvfb \
  && FIREFOX_DOWNLOAD_URL='https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64' \
  && curl -sL "$FIREFOX_DOWNLOAD_URL" | tar -xj -C /opt \
  && ln -s /opt/firefox/firefox /usr/local/bin/ \
  && BASE_URL='https://github.com/mozilla/geckodriver/releases/download' \
  && VERSION=$(curl -sL 'https://api.github.com/repos/mozilla/geckodriver/releases/latest' | grep tag_name | cut -d '"' -f 4) \
  && curl -sL "${BASE_URL}/${VERSION}/geckodriver-${VERSION}-linux64.tar.gz" | tar -xz -C /usr/local/bin \
  && apt-get purge -y \
    curl \
    bzip2 \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /tmp/* /usr/share/doc/* /var/cache/* /var/lib/apt/lists/* /var/tmp/*
  
# Copy all files
COPY ./todo_app /code/todo_app
COPY ./poetry.lock /code/
COPY ./poetry.toml /code/
COPY ./pyproject.toml /code/
COPY ./todo_app/.env /code/todo_app/.env

# Setup the entry point
ENTRYPOINT ["poetry", "run", "flask"]