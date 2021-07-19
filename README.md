# DevOps Apprenticeship: Project Exercise

## Getting started
The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:


```bash
$ poetry install
```
You'll also need to clone a new .env file from the .env.tempalate to store local configuration options. This is a one-time operation on first setup:
```bash
$ cp .env.template .env  # (first time only)
```
The .env file is used by flask to set environment variables when running flask run. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a SECRET_KEY variable which is used to encrypt the flask session cookie.

The project makes use of a MongoDB to store todo items. Create an account at www.mongodb.com and update the .env variables with relevant information below

```bash
MONGO_CONNECTION= ##replace with Mongo connection string from the Mongo dashboard. 
##This should be in the format mongodb+srv://USERNAME:PASSWORD@SERVERADDRESS/DBNAME ## 
```

## Travis CI, Docker Hub & Azure
This app uses an account at Travis CI, Docker Hub & Azure to run a CI/CD pipeline to deploy to https://ketodoapp21.azurewebsites.net/

## Githun Oauth authentication
This app uses oauth2 via github to allow logins with github credentials.
Please create a new oauth app at settings/developer settings and record the client secret and client id in the .env variables
```bash
OAUTH_SECRET=##replace with oauth secret from Github##
CLIENT_ID=##replace with client_id from Github##
```

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

## Docker 
Included is a multi-stage Dockerfile which can be used to build live, dev and test containers along with a docker-compose file to build and run the dev and test containers

First ensure you have a Docker environment and to build and run the test and dev containers simply type the following from the root folder
```bash
docker-compose up --build
```

To build the production container use a command similar to the following 
```bash
docker build --target production --tag todo-app:prod .
```
Then to run the container on port 80 of your host machine:
```bash
docker run -d -p 80:5000 --env-file todo_app/.env  todo-app:prod
```

## Vagrant 
included is a vagrantfile for provisioning a VM to run the project and dependencies
required:
download and install vagrant
download and install virtualbox

start the project by navigating to the working directory for the project and typing the following
```bash
$ vagrant up
```
Vagrant will use Gunicorn running in daemon mode to run the application in the background so you won't see the flask app load output above.
You should see output similar to the following followed by installing various dependencies:
```bash
==> default: Running action triggers after up ...
==> default: Running trigger: Launching App...
==> default: Running the TODO app setup script
    default: Running: inline script
```

gunicorn_access.log will be created to log access
gunicorn_error.log will be created to log errors