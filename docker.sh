#! /bin/bash

# install docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update

sudo su -

apt-cache policy docker-ce
sudo apt-get install -y docker-ce
sudo usermod -aG docker ubuntu
# sudo systemctl status docker

#install docker compose
# Install docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Change permission
sudo chmod +x /usr/local/bin/docker-compose

# Check the version
# docker-compose --version

#install sonar

sudo sysctl -w vm.max_map_count=262144
mkdir sonar && cd sonar 

wget https://raw.githubusercontent.com/o3cloudng/RFID/master/docker-compose.yml

sudo su ubuntu 

sudo docker–compose up
# docker ps




