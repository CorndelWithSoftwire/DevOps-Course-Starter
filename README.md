# DevOps Apprenticeship: Project Exercise

<<<<<<< HEAD
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

=======
## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### Poetry installation (Bash)
```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### On macOS and Linux
>>>>>>> my commit
```bash
$ poetry install
```

<<<<<<< HEAD
You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
=======
You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-line operation on first setup:
```bash
$ cp .env.template .env # (first time only)
```

The `.env` file is used by flask to set environment variables when running ` flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). 

In order to run this application you will require the appropriate trello information in the `.env` file. They are as follows
```
boardId=<your_board_id>
key=<your_key>
token=<your_token>
```

Once the setup script has completed and all packages have been installed, start the Flask app by running:
>>>>>>> my commit
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
<<<<<<< HEAD
=======

# Running Tests
All tests can be run with pytest using the following commands
```bash
poetry run pytest test
```
>>>>>>> my commit
