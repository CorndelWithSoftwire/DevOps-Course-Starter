#!/bin/bash

# Create and enable a virtual environment
python -m venv env
source env/bin/activate

# Upgrade pip and install required packages
pip install --upgrade pip
pip install -r requirements.txt

# Create a .env file from the .env.template
cp -n .env.template .env
