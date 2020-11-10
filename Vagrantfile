Vagrant.configure("2") do |config|
   config.vm.box = "hashicorp/bionic64"
   config.vm.provision "shell", privileged: false, inline: <<-SHELL
      sudo apt-get update

      # Install pyenv prerequisites
      sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
      libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
      xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
      # TODO: Install pyenv
   SHELL
end
