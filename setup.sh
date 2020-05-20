#!/bin/bash
Windows=0;

while [[ "$#" -gt 0 ]]; do case $1 in
  --windows) 
    Windows=1;;
esac; shift; done

# Create and enable a virtual environment
python -m venv env

if [ $Windows == 1 ]
then source env/scripts/activate
else source env/bin/activate
fi

# Upgrade pip and install required packages
pip install --upgrade pip
pip install -r requirements.txt

# Create a .env file from the .env.template
cp -n .env.template .env
