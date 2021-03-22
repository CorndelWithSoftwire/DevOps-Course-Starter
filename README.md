## System Requirements

### How to use this app
1. set the mongodb connection string variable
2. create a database called "DevOps"
3. create 3 collections as below 

```bash
MONGO_CONN=mongodb+srv://<username>:<password>@corndel.gyf3r.mongodb.net/test?w=majority 
MONGO_DB_NAME=DevOps
MONGO_LIST_TODO=todo
MONGO_LIST_INPROGRESS=inprogress
MONGO_LIST_DONE=done
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

## Heroku Deployment
docker pull rajrahman/todoapp
docker tag rajrahman/todoapp registry.heroku.com/rajrahmantodoapp/web
docker push registry.heroku.com/rajrahmantodoapp/web
heroku container:push web --app rajrahmantodoapp
heroku container:release web --app rajrahmantodoapp