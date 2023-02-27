## Running the code on a VM with SSH
wget (RAW CODE URL FROM GITHUB) <br />
Ex. wget https://raw.githubusercontent.com/nat0321/mininet/main/mininet-test.py <br />
<br />
sudo mn —custom FILENAME.py —topo=TOPONAME <br />
Ex. sudo mn —custom mininet-test.py —topo=mytopo <br />

## Starting a Mininet Docker Container
sudo docker run -it --rm --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.x11-unix -v /lib/modules:/lib/modules --name=omnet pmanzoni/mininet-in-a-container
<br /><br />
If you need to reconnect to the docker container:
<br />
sudo docker exec -it omnet bash
<br /><br />

## Starting costom topology in ONOS inside of Docker container
Find local ip of host or ONOS controler:
<br />
Finding IP of local host:
<br />
ip a
<br /><br />
Installing custom topology inside of container:
<br />
wget --no-check-certificate https://raw.githubusercontent.com/nat0321/mininet/main/OmnetTopo.py
<br /><br />
Starting Mininet with custom topology:
<br />
mn --controller remote,ip=LOCAL_IP_OF_HOST --custom OmnetTopo.py --topo=OmnetTopo
## Mininet Python API guide
<br />
http://mininet.org/api/classmininet_1_1net_1_1Mininet.html


sudo ovs-vsctl -- set Bridge s1 ipfix=@i -- --id=@i create IPFIX targets=\"172.16.234.96:2055\" obs_domain_id=123 obs_point_id=456 sampling=64
