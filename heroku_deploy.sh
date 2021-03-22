#!/bin/bash
echo "Deploying to Heroku"
docker tag todo-app:prod registry.heroku.com/todo-test-application/web
docker push registry.heroku.com/todo-test-application/web
heroku container:release web -a todo-test-application