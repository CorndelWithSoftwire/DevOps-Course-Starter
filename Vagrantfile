Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    sudo apt-get update

    # Install pyenv prerequisites
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

    # install pyenv
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    # echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    # echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile

    echo 'eval "$(pyenv init -)"' >> ~/.profile 
    
    source ~/.profile
    pyenv install 3.8.6 --skip-existing
    pyenv global 3.8.6

    # echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
   
    # echo pyenv install 3.8.6 --skip-existing >> ~/.bashrc
    # echo pyenv global 3.8.6 >> ~/.bashrc

    # source ~/.bashrc

    # echo source ~/.bashrc >> ~/.bashrc

    echo "******** INSTALL POETRY *******"

    # Install Poetry
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

    # source $HOME/.poetry/env

    # echo poetry install >> ~/.bashrc
    # echo poetry run flask run >> ~/.bashrc
    # source ~/.bashrc

    # Run final updates
    # sudo -- sh -c 'apt-get update; apt-get upgrade -y; apt-get dist-upgrade -y; apt-get autoremove -y; apt-get autoclean -y'

  SHELL

  config.trigger.after :up do |trigger|
    trigger.name = "Launching app"
    trigger.info = "Running the TODO app setup"
    trigger.run_remote = {privileged: false, inline: "
      echo ******** PYENV *******
      cd /vagrant
      # pyenv install 3.8.6 --skip-existing
      echo ******** GLOBAL *******
      # pyenv global 3.8.6
      echo ******** POETRY INSTALL *******
      poetry install
      echo ******** FLASH RUN *******
      poetry run flask run
    "}
  end


end