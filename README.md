# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### System Requirements
The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the poetry documentation):


### Installing dependencies
To install project dependency. Use the previously installed poetry cli to install required dependencies

```bash
poetry install
``` 
Ensure that local configurations are provided to flask. This should be a one time operation
```bash
cp .env.template .env
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change).
There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

### Running app
Once all setup and dependencies has completed and all packages have been installed, start the Flask app by running:
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

#### Running with Vagrant
- Download and install vagrant if not present https://safe.menlosecurity.com/https://www.vagrantup.com/docs/installation
- run `vagrant up` to start development env and start app   

how to run tests
- ensure chromedriver is downloaded and added to system path (https://chromedriver.chromium.org/downloads) 
- run `poetry run pytest` from the command line
