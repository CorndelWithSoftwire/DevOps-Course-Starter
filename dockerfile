FROM python:3.8.6-buster

# RUN apt-get update && apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
#             libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
#             xz-utils tk-dev libffi-dev liblzma-dev python-openssl git gunicorn

# RUN ["/bin/bash", "-c", "pip install poetry==1.1.4"]
# RUN ["/bin/bash", "-c", "python -m venv /venv"]
# RUN ["/bin/bash", "-c", ". /venv/bin/activate"]
# WORKDIR /project
# COPY /todo_app /project/todo_app
# COPY /tests/ /project/tests/
# COPY  poetry.lock *.toml /project/
# RUN cd /project/
# RUN ["/bin/bash", "-c", "poetry install --no-dev"]
# COPY docker-entrypoint.sh ./
# CMD ["./docker-entrypoint.sh"]
RUN apt-get update && apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
            libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
            xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
RUN pip install poetry
RUN python -m venv /venv
WORKDIR /project
COPY /todo_app /project/todo_app
COPY /tests/ /project/tests/
COPY  poetry.lock *.toml .env.test /project/
RUN cd /project/
RUN poetry install
COPY docker-entrypoint.sh ./
CMD ["./docker-entrypoint.sh"]