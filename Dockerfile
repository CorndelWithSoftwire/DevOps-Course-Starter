# Create Python Image
FROM python:3.8.4-buster as Base

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV PATH="${PATH}:/root/.poetry/bin"

# Create Workdir & Copy the Code
WORKDIR /DevOps-Course-Starter
COPY . /DevOps-Course-Starter


# Expose the Port
EXPOSE 5000

FROM base as development

#RUN poetry config virtualenvs.create false --local
RUN poetry install
ENTRYPOINT [ "poetry", "run", "flask", "run", "--port", "5000" , "--host", "0.0.0.0"]

FROM base as production

ENV FLASK_ENV=production
RUN poetry install
RUN poetry add gunicorn
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000"]