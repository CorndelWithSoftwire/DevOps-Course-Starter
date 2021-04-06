#!/bin/bash
if [ -z "$PORT" ]
then
      export PORT=5000
fi
poetry run gunicorn --config=gunicorn_config.py 'todoapp.wsgi:create_app()'
