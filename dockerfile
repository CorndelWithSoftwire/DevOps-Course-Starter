FROM python:3.8.6-buster

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.4

RUN apt-get update && apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
            libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
            xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

RUN pip install "poetry==$POETRY_VERSION"
RUN pip install gunicorn
WORKDIR /project
COPY /todo_app /project/todo_app
COPY /tests/ /project/tests/
COPY  poetry.lock *.toml .env.test /project/
RUN cd /project/
RUN poetry install
CMD  ["gunicorn", "-w 4", "todo_app.wsgi:app"]
