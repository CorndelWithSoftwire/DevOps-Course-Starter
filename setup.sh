#Step 1: sets the output if the script fails for error

#!/usr/bin/env bash

#Step2: updates the list of available resources 
sudo apt-get update -y

#Step3: Install PyEnv Requisites
sudo apt-get install -y git

#Step4: installs pip Python Version 
sudo apt-get install python3-pip

#Step5: installs poetry 
curl -sSL https://raw.githubusercontent.com/python-poetry/ \
poetry/master/get-poetry.py | python

#Step6: clone repository of To Do App code from GIT
git clone https://github.com/Shaj-Amex/DevOps-Course-Starter.git

#Step7: copy the .env file as required for running the App with provided credentials
poetry install 
cp .env.template .env
