# DevOps Apprenticeship: Project Exercise

### How to use this app
1. Obtain a key and code from Trello API, set this in the .env file
2. Get your board ID from tello and set this in the .env file
3. Obtain from trello your list id's and set these in the *_list_id variables 

```bash
trello_key=
trello_token=
trello_boardid=
todo_list_id=
doing_list_id=
done_list_id =
```
### Building Docker Image
```bash
docker build --target development --tag todoapp:dev .
docker build --target production --tag todoapp:prod .
```

## Running Docker Image as Production
To run the ToDo app as production, run the following
```bash
docker run -p 80:5000 --env-file .env -d todoapp:prod
```
Go to http://localhost:80 and you should see the ToDo app now running

## Running Docker Image as Development
To run the ToDo app as production, run the following
```bash
docker run -p 80:5000 --env-file .env --mount type=bind,source=$(pwd),target=/usr/src/app todoapp:dev
```
Go to http://localhost:80 and you should see the ToDo app now running
