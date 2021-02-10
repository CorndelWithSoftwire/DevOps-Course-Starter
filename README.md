# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

## Configuration Requirements 

The following must be done before running the Flask App. 

Create a text file, `.env`, that must have the following:
```
TRELLO_KEY=<Trello API key>
TRELLO_TOKEN=<Trello API token>
TRELLO_BOARD_ID=<Trello board id>
key=<Trello API key>
token=<Trello API token>
``` 
The file must reside in the ```todo_app``` folder.

At your Trello, create two boards, 'Not Started'  and 'Completed'.  You will need to use Postman to obtain the board's id.  This id needs to be placed in .env file (see above).

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

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

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
 * Debugger PIN: 999-999-999
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the App on a VM (Vagrant)

This project comes with a Vagrant file that allows the ToDo app to run a VM.  You will need to download and install the following two software: Virtual Box, https://www.virtualbox.org/ and Vagrant, https://www.vagrantup.com/.  Open up a terminal console, and navigate to this project folder, type:
```bash 
vagrant up
```
If this is not done before, it will take several minutes to download an Ubuntu image from hashicorp site and do various configuration.

At the end, the output should be similar in above section on Running The App.

To end the Vagrant session, CTRL-C and kill the ruby process.

## Running the App on Docker
This project also comes with a file `dockerFile` that have two profiles: `developments` and `production`

### Creating and running a container for development
In a console, run this command:

```powershell
docker build --target developments --tag todo-app:dev .
```
To run the app server from the container:
```powershell
docker run -p 5000:5000 --env-file .\.env --mount type=bind,source="$(pwd)"/todo_app,target=/project/todo_app todo-app:dev
```
If you want to run the container in background:
```powershell
docker run -d -p 5000:5000 --env-file .\.env --mount type=bind,source="$(pwd)"/todo_app,target=/project/todo_app todo-app:dev 
```

### Creating and running a container for production
In a console, run this command:

```powershell
docker build --target production --tag todo-app:prod .
```

To run the app server from the container:
```powershell
docker run -p 5000:5000 --env-file .\.env todo-app:prod
```
If you want to run the container in background:
```powershell
docker run -d -p 5000:5000 --env-file .\.env todo-app:prod 
```