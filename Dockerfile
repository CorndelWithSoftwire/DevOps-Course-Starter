FROM python:3.8-buster
WORKDIR /todo
COPY . .
RUN pip install poetry && poetry install --no-root

EXPOSE 5000

ENTRYPOINT ["poetry","run","flask","run","--host=0.0.0.0"]