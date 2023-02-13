from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import OVSKernelSwitch
from mininet.node import Host
from mininet.node import RemoteController

def emptynet():

    # Creating empty network
    net = Mininet(controller=RemoteController, waitConnected=True)

    # Adding remote ONOS controller
    c1 = net.addController('c1', controller=RemoteController, ip='172.16.235.233', port=6653)

    # Adding Hosts
    host1 = net.addHost('host1', cls=Host, ip='10.0.0.6')
    host2 = net.addHost('host2', cls=Host, ip="10.0.0.7")
    host3 = net.addHost('host3', cls=Host, ip="10.0.0.8")
    host4 = net.addHost('host4', cls=Host, ip="10.0.0.9")
    host5 = net.addHost('host5', cls=Host, ip="10.0.0.10")
    host6 = net.addHost('host6', cls=Host, ip="10.0.0.11")
    host7 = net.addHost('host7', cls=Host, ip="10.0.0.12")
    host8 = net.addHost('host8', cls=Host, ip="10.0.0.12")

    # Adding Switches
    switch1 = net.addSwitch('s1', cls=OVSKernelSwitch, ip='10.0.0.2')
    switch2 = net.addSwitch('s2', cls=OVSKernelSwitch, ip='10.0.0.3')
    switch3 = net.addSwitch('s3', cls=OVSKernelSwitch, ip='10.0.0.4')

    # Adding Links
    net.addLink(switch1, switch2)
    net.addLink(switch1, switch3)
    net.addLink(switch2, host1)
    net.addLink(switch2, host2)
    net.addLink(switch2, host3)
    net.addLink(switch3, host4)
    net.addLink(switch3, host5)
    net.addLink(switch3, host6)
    net.addLink(switch1, host7)
    net.addLink(switch1, host8)
    

    # Starting network
    net.start()

    # Ping all
    net.pingAll()

    # Enter ClI
    CLI(net)

    # Stopping Network
    net.stop()

# Main Function
setLogLevel( 'info' )
emptynet()
