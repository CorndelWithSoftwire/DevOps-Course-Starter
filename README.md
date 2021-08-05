# DevOps Apprenticeship: Project Exercise

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
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

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

## Trello 

What is Trello - Trello is a collaboration tool that organizes your projects into boards. At the moment Trello is acting as the database for our project storing our card data in the various lanes relating to their status. 

How to set up a board - Create a new board from anywhere in Trello by clicking the "+" button in the header and selecting "Create Board" in the drop-down menu. Add a new board or Workspace.

The .env.template file shows the values that you will need to extract from the Trello board/card data and this can be found using the Trello API - "https://api.trello.com/"


## Pytest 

Before running the app you can run unit and integration tests to see if the app works, the tests are found in the tests folder. 

To run unit tests run the following command - 
```
$ poetry run pytest todo_app/tests
```

## Vagrant 

To run the app using vagrant run 
```
$ vagrant up 
```
 
Prior to doing this please ensure you have VirtualBox and Vagrant installed 
Virtualbox - https://www.virtualbox.org/
Vagrant - https://www.vagrantup.com/


## Docker 

1. The container can either be built in dev or prod 
```
$ docker build --target development --tag todo-app:dev .
$ docker build --target production --tag todo-app:prod .
```

2. How to run the app with the bind mount - using a bind mount when running the container makes the project directory on your host machine available as a mounted directory within the container.
```
$ docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app
```

3. From there you can run the image in the container and specify whether you would like it to run in production or in development.
```
$ docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev
$ docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:production
```

4. To get the app to run in the container using the docker-compose.yml, with the build flag so it rebuilds the image as necessary.
```
docker-compose up --build
```

5. To stop the container  
```
docker-compose stop
```
6. To build image for the tests 
$ docker build --target test --tag my-test-image .

6. To run tests 
$ docker run my-test-image 