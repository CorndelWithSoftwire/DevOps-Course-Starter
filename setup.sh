#! /usr/bin/env bash

# Installing poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Add poetry to PATH in script
export POETRY_ROOT=\"$HOME//.poetry/\"
export PATH=\"$POETRY_ROOT/bin:$PATH\"

#Install Python
sudo apt-get update -y && sudo apt-get install -y python3.8 