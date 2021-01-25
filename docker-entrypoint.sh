#!/bin/bash
set -e

poetry run gunicorn --bind 0.0.0.0:5000 todo_app.wsgi:app
