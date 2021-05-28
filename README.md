# Docker Container :  To do list
Python code interacts with MongoDB to give a unique front end interacting with Mongo systems

OAUTH Security implemented

Getting Started

Docker image 1 (tag:  dave2): 
Gunicorn production environment, built using:
docker build --target production -f Dockerfile --tag dave2 .

Docker image 2 (tag:  davedev):
Flask development environment, built using:
docker build --target development -f Dockerfile --tag davedev .

Docker image 3 (tag:  test):
Flask test environment, built using:
docker build --target test --tag my-test-image .

## Latest Updates:  Security (oauthlib) added

## Prerequisities

To run locally, 

(poetry add oauthlib flask-login is recorded in pyproject.toml)

1)  For a security reason add this to .env file:

OAUTHLIB_INSECURE_TRANSPORT=1

then run:

In order to run this container you'll need 
1) Docker installed
2) A file, recommended called .env, that has at least below elements :

Minimum variable file:
# Flask server configuration.
FLASK_APP=app
FLASK_ENV=development

# Change the following values for local development.
SECRET_KEY=secret-key
key=   Enter value here                 NO LONGER REQUIRED (FROM OLDER VERSION)
mongopass = Enter mongo password here
FUTURE:  Will add mongoid variable into code (presently hard-coded to dev userid)

#END OF FILE

Container Parameters
--env-file                   Recommended value:       .env 
-p                           Recommended value:       5000:5000
Image name                   Recommended value:       davedev or dave2

Example:
RUN DEVELOPMENT ENVIRONMENT IMAGE:
docker run --env-file .env -p 5000:5000 davedev
RUN DEVELOPMENT ENVIRONMENT WITH BIND MOUNT FOR HOT RELOADING:
docker run --env-file .env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app davedev
RUN PRODUCTION ENVIRONMENT IMAGE:
docker run --env-file .env -p 5000:5000 dave2
RUN TESTS FOR APP:
docker run --env-file .env -p 5000:5000 my-test-image


Authors.

Dave Rawlinson

Acknowledgments

Corndel

ADDITIONAL NOTES:

To developers, original notes:

DevOps Apprenticeship: Project Exercise

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

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ flask run
```
#
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
