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
update the .env variables with relevant Trello API information

```bash
TRELLO_KEY = ##replace with Trello API Key##
TRELLO_TOKEN = ##replace with Trello API Token##
TRELLO_TODO_BOARDID = ##replace with ID of board from Trello to use with this app##

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

## Vagrant 
included is a vagrantfile for provisioning a VM to run the project and dependencies
required:
download and install vagrant
download and install virtualbox

start the project by navigating to the working directory for the project and typing the following
```bash
$ vagrant up
```