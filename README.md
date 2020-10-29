# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux
```bash
$ source setup.sh
```
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

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ flask run
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


# Tests
ensure pytest is installed
>>> pip install pytest pytest-flask
to runn all tests, navigate to the project folder and, from the command line, run the below
>>> pytest
