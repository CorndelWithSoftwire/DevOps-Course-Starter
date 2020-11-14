Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    sudo apt-get update

    # Install pyenv prerequisites
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

    # install pyenv
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile

    # echo 'eval "$(pyenv init -)"' >> ~/.profile source ~/.profile

    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
   
    echo pyenv install 3.8.6 --skip-existing >> ~/.bashrc
    echo pyenv global 3.8.6 >> ~/.bashrc

    # source ~/.bashrc

    # echo source ~/.bashrc >> ~/.bashrc

    
    # Install Poetry
    # curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

    # source $HOME/.poetry/env

    # echo poetry install >> ~/.bashrc
    # echo poetry run flask run >> ~/.bashrc
    # source ~/.bashrc

    # Run final updates
    # sudo -- sh -c 'apt-get update; apt-get upgrade -y; apt-get dist-upgrade -y; apt-get autoremove -y; apt-get autoclean -y'

  SHELL
end