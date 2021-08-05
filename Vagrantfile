Vagrant.configure("2") do |config| 
    config.vm.box = "hashicorp/bionic64"
    config.vm.network "forwarded_port", guest: 5000, host: 5000
    config.vm.provision "shell", privileged: false, inline: <<-SHELL 
        sudo apt-get update
        sudo apt-get -y install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
        git clone https://github.com/pyenv/pyenv.git ~/.pyenv
        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
        echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
        echo 'eval "$(pyenv init --path)"' >> ~/.profile
        source ~/.profile
        pyenv install 3.8.5
        pyenv global 3.8.5
        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    SHELL
    config.trigger.after :up do |trigger|
        trigger.name = "Launching App"
        trigger.info = "Running the TODO app setup script" 
        trigger.run_remote = {privileged: false, inline: "
            cd /vagrant
            poetry install
            poetry run gunicorn --daemon --error-logfile gunicorn_error.log --access-logfile gunicorn_access.log 'todo_app.app:create_app()' -b 0.0.0.0:5000
            "}
    end
end