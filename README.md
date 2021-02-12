# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On Windows (Using Git Bash)
```bash
$ source setup.sh --windows
```

# Trello API Key And Token
Ensure your .env file contains the application Trello API_KEY and TOKEN.  See example entries below:
API_KEY=358x5xx7xxx96x686983250x1x8xx8x7
TOKEN=xxx61x75051xx88x69x6xxx781x54xx885x16x8394xxx5xxx223x48xxxx19507

# Board and List ID 
These two IDs are for the sake of simplicity been hardcoded
BOARD_ID=5f5a4b008a129438843fcf0f
LIST_ID=5f5a4b008a129438843fcf10

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


# Tests
For pytest installation ensure the following line is included in your pyproject.toml under dev dependencies:
   pytest = "6.0.2"

to runn all tests, navigate to the project folder and, from the command line, run the below
>>> poetry run pytest

# VM
The option exists to run the application in VM.  Indeed a Vagranfile has been added to the project to cater such need.

# Poetry installation (Bash)
>>> curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Poetry installation (PowerShell)
>>> (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python

# Poetry Dependencies
The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:
>>> poetry install
You'll also need to clone a new .env file from the .env.template to store local configuration options. This is a one-time operation on first setup:
>>> cp .env.template .env  # (first time only)

The .env file is used by flask to set environment variables when running flask run. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a SECRET_KEY variable which is used to encrypt the flask session cookie.

# Running the App
Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
>>> poetry run flask run
You should see output similar to the following:
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590

Now visit http://localhost:5000/ in your web browser to view the app.