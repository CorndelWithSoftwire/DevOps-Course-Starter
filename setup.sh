#!/bin/bash

# Create and enable a virtual environment
python -m venv --clear env

# Upgrade pip and install required packages
pip install --upgrade pip
pip install -r requirements.txt

# Create a .venv file from the .venv.template
cp -n .env.template .env
