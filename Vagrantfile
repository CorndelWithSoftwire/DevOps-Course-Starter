# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
config.vm.network "forwarded_port", guest: 5000, host: 5000
config.vm.boot_timeout = 600
  config.vm.box = "hashicorp/bionic64"

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    sudo apt-get update

sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

curl https://pyenv.run | bash

# echo 'git clone https://github.com/pyenv/pyenv.git ~/.pyenv' >> ~.profile
# echo 'pyenv global 3.8.5' >> ~.profile

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init - )"' >> ~/.profile
echo 'cd /vagrant' >> ~/.profile
echo 'poetry install' >> ~/.profile

# eval "$(pyenv init -)"


source ~/.profile


pyenv install 3.8.5
pyenv global 3.8.5 

# echo 'pyenv init
# eval "$(pyenv init -)"

SHELL

  config.trigger.after :up do |trigger|
     trigger.name = "Launching App"
     trigger.info = "Running the TODO app setup script"
     trigger.run_remote = {privileged: false, inline: 
                           "poetry run flask run --host 0.0.0.0" 
}
  end
end
