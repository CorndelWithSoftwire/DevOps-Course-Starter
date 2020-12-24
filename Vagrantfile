Vagrant.configure("2") do |config|
    config.vm.box = "hashicorp/bionic64"
    config.vm.network "forwarded_port", guest: 5000, host: 5000
    config.vm.provision "shell", privileged: false, inline: <<-SHELL
      sudo apt-get update
  
      # Install pyenv prerequisites
      sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
      libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
      xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
  
      # install pyenv using the .profile instead of .bashrc as .bashrc is for interactive logon
      git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  
      echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
      echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
  
      echo 'eval "$(pyenv init -)"' >> ~/.profile 
      
      # Run the .profile we have just updated
      source ~/.profile
  
      # Install Pyton 3.8.6
      pyenv install 3.8.6 --skip-existing
      pyenv global 3.8.6
  
      # Install Poetry
      curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
  
      # Run final updates of software
      sudo -- sh -c 'apt-get update; apt-get upgrade -y; apt-get dist-upgrade -y; apt-get autoremove -y; apt-get autoclean -y'
  
    SHELL
  
    config.trigger.after :up do |trigger|
      trigger.name = "Launching app"
      trigger.info = "Running the TODO app setup"
      trigger.run_remote = {privileged: false, inline: "
        cd /vagrant
        poetry install
        # Setting the host ensures that port redirection takes place.
        nohup poetry run flask run --host=0.0.0.0 > logs.txt 2>&1 &
      "}
    end
  end