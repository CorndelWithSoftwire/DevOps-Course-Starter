#!/bin/bash
echo $DOCKER_PASSWORD | docker login --username $DOCKER_USER --password-stdin
docker build --target production --cache-from kevineatondevops/todo-app:latest --tag kevineatondevops/todo-app:latest --tag kevineatondevops/todo-app:$TRAVIS_COMMIT --tag registry.heroku.com/kedevopstodoapp/web .
docker push kevineatondevops/todo-app:latest
docker push kevineatondevops/todo-app:$TRAVIS_COMMIT
echo $HEROKU_API_KEY | docker login --username=_ --password-stdin registry.heroku.com
docker push registry.heroku.com/kedevopstodoapp/web
heroku container:release web -a kedevopstodoapp