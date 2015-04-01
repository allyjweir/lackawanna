$setup = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get update
SCRIPT

$dependencies = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql libpq-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev libjpeg-dev zlib1g-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-virtualenv virtualenvwrapper
SCRIPT

$preferences = <<SCRIPT
    DEBIAN_FRONTEND=cd /vagrant
    DEBIAN_FRONTEND=mkvirtualenv proj
    DEBIAN_FRONTEND=workon proj
    DEBIAN_FRONTEND=pip install -r requirements/local.txt
SCRIPT

Vagrant.configure('2') do |config|

    config.vm.provider "virtualbox" do |v|
        v.name = "lackawanna_vm"
    #    v.gui = true
    end

    config.vm.box = 'precise64'
    config.vm.box_url = "http://files.vagrantup.com/" + config.vm.box + ".box"

    config.ssh.forward_agent = true
    # Forward the dev server port
    config.vm.network :forwarded_port, host: 8080, guest: 8000
    # Forward the postgres port
    config.vm.network :forwarded_port, host: 5436, guest: 5432

    # Create a private network, which allows host-only access to the machine
    # using a specific IP.
    config.vm.network "private_network", ip: "192.168.50.4"

    config.vm.provision "shell", inline: $setup
    config.vm.provision "shell", inline: $dependencies
end
