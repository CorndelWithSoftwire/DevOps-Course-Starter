# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "hashicorp/bionic64"
    config.vm.network "forwarded_port", guest: 5000, host: 5000
    config.vm.provision "shell", privileged: false, inline: <<-SHELL
        sudo apt-get update
    SHELL

    config.trigger.after :up do |trigger|
        trigger.name = "Launching App"
        trigger.info = "Running the TODO app setup script"
        trigger.run_remote = {privileged: false, inline: "
            # Install dependencies and launch
            # Install pyenv prerequisites
            sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
            libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
            xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
            # Install pyenv
            echo 'About to set pyenv'
            if [ ! -d \"~/.pyenv\" ]; then
                git clone https://github.com/pyenv/pyenv.git ~/.pyenv
                echo 'export PYENV_ROOT=\"$HOME/.pyenv\"' >> ~/.bash_profile
                echo 'export PATH=\"$PYENV_ROOT/bin:$PATH\"' >> ~/.bash_profile
                echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval \"$(pyenv init -)\"\nfi' >> ~/.bash_profile
            fi
            echo 'About to setup venv for python'
            #if [ ! -d \"~/venv/bin/activate\" ]; then
                sudo apt-get --assume-yes install python3-venv
                python3 -m venv ~/venv
                echo 'eval \"$(pyenv init -)\"' >> ~/.bash_profile
                source ~/.profile
            #fi
                
            echo 'Source venv'
            source ~/venv/bin/activate
            pyenv version
            pyenv install 3.8.1
            pyenv global 3.8.1
            pyenv rehash

            pip install --upgrade pip
            echo 'About to get poetry'
            curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
            source ~/.poetry/env

            cd /vagrant
            echo 'About to run poetry install'
            poetry install
            flask run --host 0.0.0.0
        "}
    end
end
