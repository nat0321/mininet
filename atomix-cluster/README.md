# Automatic ONOS cluster using a Docker compose file
This compose file also automaticlly enables OpenFlow in the ONOS cluster to allow connection to Mininet
<br /><br />

**Portainer for easy GUI managment of Docker conatiners:**
<br />
`docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest`
<br /><br />
Portainer Web Interface: `https://IP:9443`

<br /><br />
To download tarball of folder:
<br />
`wget https://github.com/nat0321/mininet/raw/main/atomix-cluster/atomix-cluster.tgz`
<br />
Extract the folder: `tar xvfz atomix-cluster.tgz`
<br /><br />
Create the cluster with: `sudo docker-compose up -d`
<br />
The controllers can be accessed two ways through their Docker local IP or the hosts public IP
<br /><br />

**To acess them via their Docker local IP use the IPs listed below:**
<br />
Controller 1: `172.16.1.5`
<br />
Controller 2: `172.16.1.6`
<br />
Controller 3: `172.16.1.7`
<br />
Ports:
<br />
GUI: `8181`
<br />
CLI: `8101`
<br />
OpenFlow: `6653`
<br /><br />

**Using the hosts public IP:**
<br />
Acess the three controllers GUIs at:
<br />
Controller 1: `http://IP:8181/onos/ui`
<br />
Controller 2: `http://IP:8182/onos/ui`
<br />
Controller 3: `http://IP:8183/onos/ui`
<br /><br />
CLI Ports:
<br />
Controller 1: `8101`
<br />
Controller 2: `8102`
<br />
Controller 3: `8103`
<br /><br />
OpenFlow ports:
<br />
Controller 1: `6653`
<br />
Controller 2: `6654`
<br />
Controller 3: `6655`
<br /><br />

**To connect to ONOS CLI:**
<br />
Command: `ssh -p PORT karaf@IP`
<br />
Example: `ssh -p 8101 karaf@192.168.5.4`
<br />
Password: `karaf`

**To acess the Mininet container created in the compose file:**
<br />
`sudo docker exec -it mininet bash`
<br />
Once inside the continer run your Mininet command.
<br />
Mininet command cluster example:
<br />
`mn --controller remote,ip=IP,port=6653 --controller remote,ip=IP,port=6654 --controller remote,ip=IP,port=6655 --topo tree,3`
<br />
