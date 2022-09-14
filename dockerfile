FROM python:3.7 as pyhome

WORKDIR /app

COPY todo_app ./todo_app/
COPY pyproject.toml .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry add gunicorn

RUN apt-get update && apt-get upgrade -y

EXPOSE 5000

FROM pyhome as devpy
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM pyhome as devtestpy
ENTRYPOINT poetry run pytest

FROM pyhome as prodpy               
CMD poetry run gunicorn "todo_app.app:create_app()" --bind 0.0.0.0:${PORT:-5000}


