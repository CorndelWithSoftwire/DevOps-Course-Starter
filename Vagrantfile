Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    sudo apt-get update

    # Install pyenv prerequisites
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

    # install pyenv (already in my image)
    # git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    # echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    # echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

    # echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
    # exec "$SHELL"

    # TODO: Install pyenv prerequisites 
    # TODO: Install pyenv
  SHELL
end