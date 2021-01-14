#!/bin/bash
set -e

. /venv/bin/activate

exec gunicorn --bind 0.0.0.0:5000 todo_app.wsgi:app