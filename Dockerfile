# Perform common operations, dependency installation etc...
FROM python:3.8-slim-buster as base
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

# Install curl
# RUN apt-get update && apt-get install -y curl

# # Install the latest version of Firefox:
# RUN export DEBIAN_FRONTEND=noninteractive && apt-get update \
#   && apt-get install --no-install-recommends --no-install-suggests --assume-yes \
#     curl \
#     bzip2 \
#     libgtk-3-0 \
#     libdbus-glib-1-2 \
#     xvfb \
#   && FIREFOX_DOWNLOAD_URL='https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64' \
#   && curl -sL "$FIREFOX_DOWNLOAD_URL" | tar -xj -C /opt \
#   && ln -s /opt/firefox/firefox /usr/local/bin/ \
#   && BASE_URL='https://github.com/mozilla/geckodriver/releases/download' \
#   && VERSION=$(curl -sL 'https://api.github.com/repos/mozilla/geckodriver/releases/latest' | grep tag_name | cut -d '"' -f 4) \
#   && curl -sL "${BASE_URL}/${VERSION}/geckodriver-${VERSION}-linux64.tar.gz" | tar -xz -C /usr/local/bin \
#   && apt-get purge -y \
#     curl \
#     bzip2 \
#   && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
#   && rm -rf /tmp/* /usr/share/doc/* /var/cache/* /var/lib/apt/lists/* /var/tmp/*

ENTRYPOINT ["poetry", "run", "pytest"]