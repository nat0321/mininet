from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import OVSKernelSwitch
from mininet.node import Host

def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller, waitConnected=True )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    host1 = net.addHost('PV1', cls=Host, ip='10.0.0.2')
    host2 = net.addHost('PV2', cls=Host, ip='10.0.0.3')
    host3 = net.addHost('PV3', cls=Host, ip='10.0.0.5')
    host4 = net.addHost('PV4', cls=Host, ip='10.0.0.7')
    host5 = net.addHost('PV5', cls=Host, ip='10.0.0.9')
    host6 = net.addHost('LD1', cls=Host, ip='10.0.0.1')
    host7 = net.addHost('LD2', cls=Host, ip='10.0.0.4')
    host8 = net.addHost('LD3', cls=Host, ip='10.0.0.6')
    host9 = net.addHost('LD4', cls=Host, ip='10.0.0.8')
    host10 = net.addHost('LD5', cls=Host, ip='10.0.0.10')
    host11 = net.addHost('PDC', cls=Host, ip='10.0.0.12')
    host12 = net.addHost('BAT1', cls=Host, ip='10.0.0.11')
    host13 = net.addHost('CVRC', cls=Host, ip='10.0.0.14')
    host14 = net.addHost('PMU1', cls=Host, ip='10.0.0.13')

    info( '*** Adding switch\n' )
    switch1 = net.addSwitch('s1', cls=OVSKernelSwitch, ip='10.0.0.22')
    switch2 = net.addSwitch('s2', cls=OVSKernelSwitch, ip='10.0.0.57')

    info( '*** Creating links\n' )
    net.addLink(host1, switch2)
    net.addLink(host2, switch2)
    net.addLink(host3, switch2)
    net.addLink(host4, switch2)
    net.addLink(host5, switch2)
    net.addLink(host6, switch2)
    net.addLink(host7, switch2)
    net.addLink(host8, switch2)
    net.addLink(host9, switch2)
    net.addLink(host10, switch2)
    net.addLink(host11, switch1)
    net.addLink(host12, switch2)
    net.addLink(host13, switch2)
    net.addLink(host14, switch2)
    net.addLink(switch1, switch2)

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    host1.cmdPrint('iperf -s &')
    host2.cmdPrint('iperf -c 10.0.0.2')
    net.iperf()

    #info( '*** Stopping network\n' )
    #net.stop()
    CLI(net)


if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()