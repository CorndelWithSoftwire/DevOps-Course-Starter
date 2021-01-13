#!/bin/bash
poetry run gunicorn --config=gunicorn_config.py 'todoapp.wsgi:create_app()'
