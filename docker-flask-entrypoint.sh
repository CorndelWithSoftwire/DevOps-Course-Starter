#!/bin/bash
set -e

#. /venv/bin/activate

poetry run flask run --host 0.0.0.0 --port 5000
