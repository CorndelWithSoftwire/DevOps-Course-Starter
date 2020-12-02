FROM python:3.7 as base
RUN mkdir /app
COPY pyproject.toml poetry.toml poetry.lock /app/
WORKDIR /app
RUN pip3 install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

FROM base as development
WORKDIR /app
EXPOSE 5000/tcp
CMD ["poetry", "run", "flask", "run", "-h", "0.0.0.0"]

FROM base as production
COPY . /app/
WORKDIR /app
EXPOSE 8000/tcp
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0", "app:create_app()"]

FROM base as test
WORKDIR /app
CMD ["poetry", "run", "pytest"]