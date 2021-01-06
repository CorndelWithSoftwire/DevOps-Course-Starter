# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "hashicorp/bionic64"
    config.vm.network "forwarded_port", guest: 5000, host: 5000
    config.vm.provision "shell", privileged: false, inline: <<-SHELL
        sudo apt-get update
        # Install dependencies and launch
        # Install pyenv prerequisites
        sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
        libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
        xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

        # Install pyenv
        if [ ! -d \"$HOME/.pyenv\" ]; then
            git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv                  
        fi

        export PYENV_ROOT=\"$HOME//.pyenv/\"
        export PATH=\"$PYENV_ROOT/bin:$PATH\"
        pyenv init
        pyenv version
        pyenv install 3.8.1
        pyenv global 3.8.1
        pyenv rehash
        git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
        pyenv virtualenv venv
        source $HOME/.pyenv/versions/venv/bin/activate
        pip install --upgrade pip

        echo "About to get poetry"
        cd /vagrant
        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
        source $HOME/.poetry/env
        echo 'About to run poetry install'
        poetry install

    SHELL

    config.trigger.after :up do |trigger|
        trigger.name = "Launching App"
        trigger.info = "Running the TODO app setup script"
        trigger.run_remote = {privileged: false, inline: "
            source $HOME/.pyenv/versions/venv/bin/activate
            cd /vagrant
            flask run --host 0.0.0.0
        "}
    end
end
