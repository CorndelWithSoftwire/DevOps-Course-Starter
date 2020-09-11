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

## Running the Application

Once the setup script has completed and you've setup trello as bove, start the Flask app by running:
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
