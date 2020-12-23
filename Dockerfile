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
COPY tests /app/tests
COPY .env.test /app
WORKDIR /app
CMD ["poetry", "run", "pytest", "tests/test_viewmodel.py", "tests/test_integration.py"]