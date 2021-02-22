FROM python:3.7 as base
RUN mkdir /app
COPY *.toml /app/
WORKDIR /app
RUN pip3 install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

FROM base as development
WORKDIR /app
EXPOSE 5000/tcp
CMD ["poetry", "run", "flask", "run", "-h", "0.0.0.0"]

FROM base as production
COPY . /app
WORKDIR /app
EXPOSE 8000/tcp
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0", "todo_app.app:create_app()"]

FROM base as test
COPY . /app
WORKDIR /app
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb \
    && apt-get update \
    && apt-get -f install ./chrome.deb -y \
    && rm ./chrome.deb
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` \
    && echo "Installing chromium webdriver version ${LATEST}" \
    && curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip \
    && apt-get install unzip -y \
    && unzip ./chromedriver_linux64.zip
CMD ["poetry", "run", "pytest"]