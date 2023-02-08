## Running the code on a VM with SSH
wget (RAW CODE URL FROM GITHUB) <br />
Ex. wget https://raw.githubusercontent.com/nat0321/mininet/main/mininet-test.py <br />
<br />
sudo mn —custom FILENAME.py —topo=TOPONAME <br />
Ex. sudo mn —custom mininet-test.py —topo=mytopo <br />

## Starting the Docker Container
sudo docker run -it --rm --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.x11-unix -v /lib/modules:/lib/modules --name=omnet pmanzoni/mininet-in-a-container
<br /><br />
If you need to reconnect to the docker container:
<br />
sudo docker exec -it omnet bash
<br /><br />

## Starting costom topology in ONOS inside of Docker container
Find local ip of host:
<br />
ip a
<br /><br />
mn --controller remote,ip=LOCAL_IP_OF_HOST --custom OmnetTopo.py --topo=OmnetTopo
