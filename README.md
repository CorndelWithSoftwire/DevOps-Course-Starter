# DevOps Apprenticeship: Project Exercise

[![Build Status](https://www.travis-ci.com/jatin-28/DevOps-Course-Starter.svg?branch=master)](https://www.travis-ci.com/jatin-28/DevOps-Course-Starter)

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install --no-dev
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

### Notes

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change).

APP_API_KEY - This is the Trello API key which you can obtain from [here](https://trello.com/app-key)
APP_TOKEN - This is the Trello APP token which you can be obtained by clicking the create manual Token link on the same page as fetching the app key

Create a trello TODO board with 2 lists and obtain their IDs and set in the environment variables below

TODO_BOARD_ID 

### Running tests locally

```bash
PYTHONPATH=. pytest tests
```

#### Just Unit tests
```bash
PYTHONPATH=. pytegit pushst tests/unit
```

#### Just Integration tests
```bash
PYTHONPATH=. pytest tests/integration
```

## Running the App Locally

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.


### gunicorn support
Support for gunicorn local run 
```
$ poetry run gunicorn --daemon --bind 0.0.0.0:5000 -w 1 "wsgi:create_app()"
```

### Vagrant
You can also use vagrant
```
$ vagrant up
```

### Docker Compose

```
$ docker-compose build && docker-compose up -d <target>
```

### Docker

Building and running development 
```
$ docker build --target development --tag todo-app:dev .
$ docker run --env-file ./.env -p 5100:5000 --mount type=bind,source="$(pwd)/todoapp",target=/app/todoapp todo-app:dev
```

Building and running production 
```
$ docker build --target production --tag todo-app:prod .
$ docker run --env-file ./.env -p 5200:5000 todo-app:prod
```

Building and running tests 
```

# unit tests
$ docker build --target unittests --tag todo-app:unittests .
$ docker run todo-app:unittests

# integration tests
$ docker build --target integrationtests --tag todo-app:integrationtests .
$ docker run --env-file ./.env.test todo-app:integrationtests

# endtoend tests
$ docker build --target endtoendtests --tag todo-app:endtoendtests .
$ docker run --env-file ./.env todo-app:endtoendtests
```
