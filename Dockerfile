# Create Python Image
FROM python:3.8.4-buster as Base

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV PATH="${PATH}:/root/.poetry/bin"

# Create Workdir & Copy the Code
WORKDIR /DevOps-Course-Starter
COPY . /DevOps-Course-Starter

RUN poetry install

# Expose the Port
EXPOSE 5000
ENTRYPOINT [ "poetry", "run", "flask", "run", "--port", "5000" , "--host", "0.0.0.0"]