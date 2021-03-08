#! /usr/bin/env bash

# Installing poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Add poetry to PATH in script
export POETRY_ROOT=\"$HOME//.poetry/\"
export PATH=\"$POETRY_ROOT/bin:$PATH\"

#Checking if poetry is already installed
poetry --version 

#Install Python
sudo apt-get update -y && sudo apt-get install -y python3.8 

#Store local variables 
cp .env.template .env 

# Run the application
poetry run flask run 

# MEntion in readme about script and how to use 