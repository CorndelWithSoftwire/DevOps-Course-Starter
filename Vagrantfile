Vagrant.configure("2") do |config|
 config.vm.box = "hashicorp/bionic64"
end

 config.vm.provision "shell", privileged: false, inline: <<-SHELL
 sudo apt-get update
 # TODO: Install pyenv prerequisites
 # TODO: Install pyenv
 SHELL