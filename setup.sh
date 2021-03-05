#! /usr/bin/env bash

# Installing poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Add poetry to PATH in script

#Checking if poetry is already installed
poetry --version 

#Install Python
sudo apt-get update -y && sudo apt-get install -y python3.8 

# Run the application

poetry run flask run 

# Message prompt - when finished run the run.sh script
# MEntion in readme about script and how to use 