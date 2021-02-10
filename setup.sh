#sets the condition for the script to stop on error
shebang | -ex

#updates the list of available resources 
sudo apt-get update -y

#installs the PyEnv requisites 
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

#installs Python
sudo apt-get install python3-pip

#installs poetry 
curl -sSL https://raw.githubusercontent.com/python-poetry/
poetry/master/get-poetry.py | python

#clone repository of App code
git clone https://github.com/tobyr84/Project-1.git 

#sets the dependances 
poetry install 
cp .env.template .env

#user to input credentials into the .env file to enable access Trello
