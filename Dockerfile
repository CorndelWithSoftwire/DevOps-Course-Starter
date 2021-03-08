FROM python:3.8.6-slim-buster as base


RUN pip install poetry
WORKDIR /project

FROM base as production
COPY  poetry.lock pyproject.toml /project/
COPY docker-entrypoint.sh ./
RUN cd /project/
RUN poetry install --no-dev
CMD ["./docker-entrypoint.sh"]

FROM base as developments
COPY /tests/ /project/tests/
COPY  poetry.lock pyproject.toml /project/
COPY docker-flask-entrypoint.sh ./docker-entrypoint.sh
RUN cd /project/
RUN poetry install
CMD ["./docker-entrypoint.sh"]

FROM base as test
RUN apt-get update && apt-get install curl fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 libdbus-1-3 libdrm2 libgbm1 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libx11-6 libxcb1 libxcomposite1 libxdamage1 libxshmfence1 wget xdg-utils -y 
RUN apt-get install fonts-liberation libasound2 
COPY /tests/ /project/tests/
COPY /tests_e2e/ /project/tests_e2e/
COPY  poetry.lock pyproject.toml /project/
COPY docker-flask-entrypoint.sh ./docker-entrypoint.sh
RUN cd /project/
RUN poetry install
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
    #apt-get -f install ./chrome-deb -y &&\
    dpkg -i ./chrome.deb &&\
    rm ./chrome.deb
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
   echo "Installing chromium webdriver version ${LATEST}" &&\
   curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
   apt-get install unzip -y &&\
   unzip ./chromedriver_linux64.zip
#CMD ["./docker-entrypoint.sh"]
ENTRYPOINT ["poetry", "run", "pytest"]