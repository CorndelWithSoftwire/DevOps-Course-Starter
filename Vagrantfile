Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"

  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = true
  end

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    sudo apt-get update 

    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
          libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
          xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

    #sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    #curl -sSL https://raw.githubusercontent.com/python-poetry/ poetry/master/get-poetry.py | python -

    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

    exec "$SHELL"
    pyenv install 3.8.3
    pyenv global 3.8.3
    python --version

    curl -sSL https://raw.githubusercontent.com/python-poetry/ poetry/master/get-poetry.py | python -
    exec "$SHELL"

    SHELL
    
    $script = <<-SCRIPT
      cd /vagrant
      poetry install
      poetry run flask run --host='0.0.0.0'
    SCRIPT

    config.trigger.after :up do |trigger|
      trigger.name = "Launching App"
      trigger.info = "Running the TODO app setup script"
      trigger.run_remote = {privileged: false, inline: $script}
      #trigger.run_remote = {privileged: false, inline: "bash -c 'cd /vagrant; poetry install; poetry run flask run --host='0.0.0.0' &&'"}
    end

  config.vm.network "forwarded_port", guest: 5000, host: 5000

end
