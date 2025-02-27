# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Define the first web server (web01) with Ubuntu 20.04
  config.vm.define "web01" do |web01|
    web01.vm.box = "ubuntu/focal64"
    web01.vm.hostname = "web01.local"
    web01.vm.network "private_network", ip: "192.168.56.101"
  
    web01.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = 1
    end
  end
  
  # Define the second web server (web02) with Ubuntu 20.04
  config.vm.define "web02" do |web02|
    web02.vm.box = "ubuntu/focal64"
    web02.vm.hostname = "web02.local"
    web02.vm.network "private_network", ip: "192.168.56.102"
  
    web02.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = 1
    end
  end
  
  # Define the database server (db01) with CentOS 7
  config.vm.define "db01" do |db01|
    db01.vm.box = "centos/7"
    db01.vm.hostname = "db01.local"
    db01.vm.network "private_network", ip: "192.168.56.103"
  
    db01.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 2
    end
  
    # Provisioning script for db01
    db01.vm.provision "shell", inline: <<-SHELL
      yum install -y wget unzip mariadb-server -y
      systemctl start mariadb
      systemctl enable mariadb
    SHELL
  end
  end

