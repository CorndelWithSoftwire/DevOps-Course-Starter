FROM python AS base
RUN pip install poetry
WORKDIR /app
COPY . .
RUN poetry install
ENTRYPOINT poetry run flask run --host=0.0.0.0


FROM base as production
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host=0.0.0.0
# Configure for production

FROM base as development
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host=0.0.0.0
# Configure for local development

FROM base as test

ENTRYPOINT poetry run pytest
