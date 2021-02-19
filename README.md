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

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change)

## Setting up Trello

You'll need a Trello account to run this project. You will need:
* API key & token
* Create a board to link this app to
* On the board, create the following lists:
    * Todo
    * Doing
    * Done

After doing this, you'll need to fill in the empty values in the `.env` file that is created by running the setup script.
* You may want to use postman to obtain these ids


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

## Running the Tests
Tests are added for Unit, Integration, Selenium Tests
To run the tests using Poetry and Pytest
```bash
$ poetry run pytest
```

## Running the App in Docker using Dockerfile
 To build the image:

1. To run the docker file in dev mode:	     
```
docker build --target development --tag todo-app:dev .
```

To run the docker file in dev mode: 
```     
docker run --env-file ./.env -p 5000:5000 todo-app:dev
```
Then Navigate to localhost:5000 
   
2. To build the docker file in prod mode:  
```  
docker build --target production --tag todo-app:prod .
```
To run the docker file in prod mode:  
```     
docker run --env-file ./.env -p 5000:80 todo-app:prod
```
Then navigate to http://0.0.0.0:5000/

3. To test local setup on UNIX:
```
docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)",target=/app/ todo-app:dev
```

## Running the test folder in dockeer
First build the docker image with a tag name my-test-image
```
docker build --target test --tag my-test-image .
```
Then run the tests with either of the following:
--To run all 
```
docker run my-test-image tests
```
--To run selenium only while passing env variables for credentials
```
docker run --env-file ./.env my-test-image tests/test_selenium.py
```
--To run unit or ntegrationn test while passing file name
```
docker run --env-file ./.env my-test-image tests/test_view_model.py
```


## Running the App  using Docker compose
```
docker-compose up --build
```


