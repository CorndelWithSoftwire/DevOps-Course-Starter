Vagrant.configure("2") do |config|
   config.vm.box = "hashicorp/bionic64"
   config.vm.provision "shell", privileged: false, inline: <<-SHELL
   sudo apt-get update

   # TODO: Install pyenv prerequisites
      sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
      libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
      xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

   # TODO: Install pyenv
      git clone https://github.com/pyenv/pyenv.git /home/vagrant/.pyenv 
      echo 'export PYENV_ROOT="/home/vagrant/.pyenv"' >> /home/vagrant/.profile
      echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> /home/vagrant/.profile
      echo 'eval "$(pyenv init -)"' >> /home/vagrant/.profile
      export PYENV_ROOT="/home/vagrant/.pyenv"
      export PATH="$PYENV_ROOT/bin:$PATH"
      eval "$(pyenv init -)"

   # Install Python 3.8.3
      pyenv install 3.8.3
      pyenv global 3.8.3

   # install poetry
      curl -sSL https://raw.githubusercontent.com/python-poetry/
      poetry/master/get-poetry.py | python

 SHELL
end