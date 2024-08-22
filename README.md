# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
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

```git remote -v ```
tells us / lists our remotes


### See below for how to build the two docker images 
```
docker build --target development --tag todo-app:dev .
docker build --target production --tag todo-app:prod .
```
### Command to run the production container
``` 
docker run --env-file .env -it -p 5001:5000 todo-app:prod
```
This command pases through the environment variables with the `--env-file` flag, and the `-it` flags make it easier to interact with the container (e.g. allowing us to shut it down with ctrl+c from our host terminal). With the `-p` flag, the app can be accessed at the address `http://localhost:5001`.

### Command to run dev container
``` 
docker run --env-file .env -it -p 5001:5000 --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev
```
Bind mount is miroring a folder and the folder in this instance is the todo app folder allowing changes to the code without having to rebuild the container. Running dev changes without having to access the container 

### Running Pytest
```bash
poetry run pytest
```


### Azure Hosting 
The container image that is deployed on Azure is hosted on Docker Hub at https://hub.docker.com/repository/docker/nashussain76/todo-app/general

The website is hosted at https://nashusappservice.azurewebsites.net/

To update the website you will need to run the following commands to build and push the updated container image:
```Bash
docker build --target production --tag nashussain76/todo-app:prod .
docker push nashussain76/todo-app:prod
```
Next you will need to make a POST request to the webhook link provided on the App Service (under the Deployment Centre tab)> This will trigger Azure to pull the updated image from Docker Hub (link not provided as it includes credentials)


