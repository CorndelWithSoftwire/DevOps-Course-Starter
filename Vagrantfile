Vagrant.configure("2") do |config|
   config.vm.box = "hashicorp/bionic64"
   config.vm.network "forwarded_port", guest: 5000, host: 5000
   config.vm.provision "shell", privileged: false, inline: <<-SHELL
      sudo apt-get update

      # Install pyenv prerequisites
      sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
      libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
      xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
      
      # Install pyenv
      git clone https://github.com/pyenv/pyenv.git ~/.pyenv
      # Set pyenv variables
      echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
      echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
      echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.profile
      
      #load variables to the current shell
      source ~/.profile
      #install python using pyenv
      pyenv install 3.8.6
      pyenv global 3.8.6
      
      #Download and install Poetry
      curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
      
   SHELL

      config.trigger.after :up do |trigger|
      trigger.name = "Launching App"
      trigger.info = "Running the TODO app setup script"
      trigger.run_remote = {privileged: false, inline: "
         cd /vagrant
         poetry install
         poetry run gunicorn --config gunicorn.conf.py 'app:create_app()'
      "}
   end
end