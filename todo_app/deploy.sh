#!/bin/bash
echo $DOCKER_PASSWORD | docker login --username $DOCKER_USER --password-stdin
docker build --target production --cache-from kevineatondevops/todo_app:latest --tag kevineatondevops/todo-app:latest --tag kevineatondevops/todo-app:$TRAVIS_COMMIT --tag registry.heroku.com/kedevopstodoapp/web .
docker push kevineatondevops/todo-app:latest
docker login --username=_ --password=$(heroku auth:token) registry.heroku.com
docker push registry.heroku.com/kedevopstodoapp/web
heroku container:release web -a kedevopstodoapp