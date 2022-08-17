# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
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

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
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

### create a place to store data for todo app

*create a trello account

*create a trello board to store todo app item data

*create a "to do" and "done" list.(you will have the option to create a "doing" list but this can be left blank)

*go to trell.com/api-key do access api key and token

*get the to do and done list id's and the board id. I did this with hoptscotch 

*to get board ID REQUIRES API TOKEN AND KEY- https://api.trello.com/1/members/me/boards?key=***KEY***&token=***TOKEN***.......

*to get the list id's, MUST ADD VAVIABLES KEY, TOKEN, CARDS  https://api.trello.com/1/boards/***BoardID***/lists

*add these to the environment file, REMEMBER virtual machines may reset this file if configured to do so.

### app testing

to check everything is working  you can use the unit tests to prove get_items is presenting the information correctly. 

if not already install pytest then poetry run pytest in the command terminal

MODULE 5

Dockerfile:
RUN poetry config virtualenvs.create false - this is because virtualenvs is included automatically but not needed as docker is in isolation.
RUN poetry install --without dev to exclude dependancy from instalation
