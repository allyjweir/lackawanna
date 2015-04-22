$setup = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get update
SCRIPT

# Development Specific Dependencies
# These are only needed in the development environment so are excluded from the project's included Aptfile
$development_dependencies = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql libpq-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev libjpeg-dev zlib1g-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-virtualenv virtualenvwrapper
SCRIPT

$application_dependencies = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get -q -y install $(cat /vagrant/Aptfile)
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
    end

    config.vm.box = 'precise64'
    config.vm.box_url = "http://files.vagrantup.com/" + config.vm.box + ".box"

    config.ssh.forward_agent = true
    # Forward the dev server port
    config.vm.network :forwarded_port, host: 8000, guest: 8000
    # Forward the postgres port
    config.vm.network :forwarded_port, host: 5436, guest: 5432

    # Create a private network, which allows host-only access to the machine
    # using a specific IP.
    config.vm.network "private_network", ip: "192.168.50.4"

    config.vm.provision "shell", inline: $setup
    config.vm.provision "shell", inline: $development_dependencies
    config.vm.provision "shell", inline: $application_dependencies
    # config.vm.provision "shell", inline: $preferences

end
