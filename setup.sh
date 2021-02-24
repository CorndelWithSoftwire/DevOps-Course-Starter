#Step 1: sets the output if the script fails for error
shebang | -ex

#Step2: updates the list of available resources 
sudo apt-get update -y

#Step3: Install PyEnv Requisites
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

#Step3: installs Python Version 
sudo apt-get install python3-pip

#Step4: Find the Python Version
python --version

#Step5: installs poetry 
curl -sSL https://raw.githubusercontent.com/python-poetry/
poetry/master/get-poetry.py | python

#Step6: Check for installed Poetry Version

poetry --version

#Step7: clone repository of To Do App code from GIT
git clone https://github.com/Shaj-Amex/DevOps-Course-Starter.git

#Step8: copy the .env file as required for running the App with provided credentials
poetry install 
cp .env.template .env
