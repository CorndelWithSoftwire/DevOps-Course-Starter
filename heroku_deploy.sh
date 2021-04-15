#!/bin/bash
echo "Deploying app to Heroku";
echo "Tagging heroku docker image";
docker tag $DOCKER_USERNAME/todo-app registry.heroku.com/$HEROKU_APP_NAME/web;
echo "LOGGING IN TO HEROKU";
echo "$HEROKU_API_KEY" | docker login -u "$HEROKU_LOGIN" --password-stdin registry.heroku.com;
echo "Pushing to Heroku docker registry";
docker push registry.heroku.com/$HEROKU_APP_NAME/web;
echo "releasing application";
heroku container:release web -a $HEROKU_APP_NAME;