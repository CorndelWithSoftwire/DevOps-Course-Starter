#!/bin/bash
echo $DOCKER_PASSWORD | docker login --username $DOCKER_USER --password-stdin
docker build --target production --cache-from kevineatondevops/todo-app:latest --tag kevineatondevops/todo-app:latest --tag kevineatondevops/todo-app:$TRAVIS_COMMIT .
docker push kevineatondevops/todo-app:latest
docker push kevineatondevops/todo-app:$TRAVIS_COMMIT
docker push registry.heroku.com/kedevopstodoapp/web
curl -dH -X POST $AZURE_WEBHOOK