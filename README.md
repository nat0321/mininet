## Running the code on a VM with SSH
wget (RAW CODE URL FROM GITHUB) <br />
Ex. wget https://raw.githubusercontent.com/nat0321/mininet/main/mininet-test.py <br />
<br />
sudo mn —custom FILENAME.py —topo=TOPONAME <br />
Ex. sudo mn —custom mininet-test.py —topo=mytopo <br />

## In Docker
sudo docker run -it —rm --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.x11-unix -v /lib/modules:/lib/modules --name=omnet pmanzoni/mininet-in-a-container

mn --controller remote, ip=172.16.234.29,port=6653 --topo torus, 3,3 --switch ovs 
sudo docker exec -it omnet bash
