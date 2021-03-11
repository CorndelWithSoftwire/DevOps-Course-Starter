# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

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

## Trello Setup
Setup the below Environment variables for Trello API
```
TRELLO_KEY
TRELLO_TOKEN
TRELLO_BOARD_ID
TRELLO_TODO_LIST_ID
TRELLO_DOING_LIST_ID
TRELLO_DONE_LIST_ID
```

Install geckodriver and Firefox as we need these two for running selenium tests.


## Running within Docker

### Building docker image
To build the docker image run the following command

```
docker build --target dev --tag todo-app:dev .
docker build --target prod --tag todo-app:prod .
```

### Running the container

To run the production container as a daemon run following command
```
docker run -p 5000:5000 --env-file .env -d todo-app:prod
```

To run the development container as a daemon ensure you mount the project directory within the container e.g. run following command
```
docker run -p 5000:5000 --env-file .env --mount type=bind,source=$(pwd),target=/code/todo_app -d todo-app:dev
```

### Documentation

C4 diagrams have been provided for this application in the files context.drawio, container.drawio and component.drawio.
These can be viewed at https://app.diagrams.net/


You should see output similar to the following:
```bash
 * Serving Flask app "todo_app/todo_app/app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.


### Heroku deployment
Commands to build and deploy to heroku
```

docker build --target test --tag my-test-image .
docker run my-test-image todo_app/test_tasks.py
docker run -e TRELLO_KEY=$TRELLO_KEY -e TRELLO_TOKEN=$TRELLO_TOKEN -e TRELLO_BOARD_ID=$TRELLO_BOARD_ID -e 
    TRELLO_TODO_LIST_ID=$TRELLO_TODO_LIST_ID -e TRELLO_DOING_LIST_ID=$TRELLO_DOING_LIST_ID -e TRELLO_DONE_LIST_ID=$TRELLO_DONE_LIST_ID my-test-image todo_app/test_client.py
docker run -e TRELLO_KEY=$TRELLO_KEY -e TRELLO_TOKEN=$TRELLO_TOKEN -e TRELLO_BOARD_ID=$TRELLO_BOARD_ID -e       
    TRELLO_TODO_LIST_ID=$TRELLO_TODO_LIST_ID -e TRELLO_DOING_LIST_ID=$TRELLO_DOING_LIST_ID -e TRELLO_DONE_LIST_ID=$TRELLO_DONE_LIST_ID   my-test-image todo_app/test_system.py
docker build --target prod --tag $DOCKER_USER/todo-app:latest .  
docker push $DOCKER_USER/todo-app:latest
docker tag $DOCKER_USER/todo-app:latest registry.heroku.com/$HEROKU_APP/web
docker push registry.heroku.com/$HEROKU_APP/web
heroku login
heroku container:release web --app=todo-app-pv
```
Note: Setup up the Trello related environment varaibles and PORT (for heroku) in Config Vars section on heroku app settings (https://dashboard.heroku.com/apps/todo-app-pv/settings)