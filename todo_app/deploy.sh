#!/bin/bash
echo $DOCKER_PASSWORD | docker login --username $DOCKER_USER --password-stdin
docker build --target production --tag kevineatondevops/todo-app:latest --tag kevineatondevops/todo-app:$TRAVIS_COMMIT .
docker push kevineatondevops/todo-app:latest