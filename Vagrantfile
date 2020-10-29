# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  config.vm.box = "hashicorp/bionic64"

  config.vm.network "forwarded_port", guest: 5000, host: 5001

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
          sudo apt-get update

          echo "Install pyenv prerequisites"
          sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
          libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
          xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

          echo "Install pyenv"

          git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv || true

          echo 'export PYENV_ROOT=$HOME/.pyenv' >> ~/.profile
          echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
          echo 'eval "$(pyenv init -)"' >> ~/.profile
          source ~/.profile

          echo "pyenv install python"
          pyenv install 3.7.7
          pyenv global 3.7.7
          
          echo "Install poetry "
          curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
       
    SHELL

    config.trigger.after :up do |trigger|
        trigger.name = "Launching App"
        trigger.info = "Running the TODO app setup script"
        trigger.run_remote = { privileged: false, inline: "
              echo 'Install poetry dependencies and launch gunicorn'
              cd /vagrant
              
              echo 'Install gunicorn'
              poetry add gunicorn
              
              echo 'Install todo app'
              poetry install --no-dev
              
              sudo mkdir -p /var/log/gunicorn
              sudo chown vagrant:vagrant /var/log/gunicorn
              poetry run gunicorn --daemon --bind 0.0.0.0:5000 -w 1 'wsgi:create_app()' --error-logfile /var/log/gunicorn/gunicorn_error.log, --log-file /var/log/gunicorn/gunicorn.log
              echo 'Launched on host http://localhost:5001'
        "}
    end

end
