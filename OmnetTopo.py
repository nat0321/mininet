from mininet.node import Controller
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import IVSSwitch
from mininet.node import OVSKernelSwitch, UserSwitch, Switch
from mininet.node import OVSController, OVSSwitch, Controller
from mininet.node import RemoteController
from mininet.log import setLogLevel, info

#changes
import sys
sys.path.append('/home/mininet/.local/lib/python3.8/site-packages')

#import pandas as pd
#from nfstream import NFStreamer
#from collections import defaultdict

#from scapy.base_classes import Net
#from scapy.all import *

import random

c1= RemoteController(name='c0', controller='RemoteController', ip='192.168.2.248', port=6653)
	

class MyTopo(Topo):
    "Simple topology example."
    def __init__(self):
        "Create custom topo."
        # Initialize topology
        Topo.__init__(self)
        host1 = self.addHost('PV1', cls=Host, ip='10.0.0.2')
        host2 = self.addHost('PV2', cls=Host, ip='10.0.0.3')
        host3 = self.addHost('PV3', cls=Host, ip='10.0.0.5')
        host4 = self.addHost('PV4', cls=Host, ip='10.0.0.7')
        host5 = self.addHost('PV5', cls=Host, ip='10.0.0.9')
        host6 = self.addHost('LD1', cls=Host, ip='10.0.0.1')
        host7 = self.addHost('LD2', cls=Host, ip='10.0.0.4')
        host8 = self.addHost('LD3', cls=Host, ip='10.0.0.6')
        host9 = self.addHost('LD4', cls=Host, ip='10.0.0.8')
        host10 = self.addHost('LD5', cls=Host, ip='10.0.0.10')
        host11 = self.addHost('PDC', cls=Host, ip='10.0.0.12')
        host12 = self.addHost('BAT1', cls=Host, ip='10.0.0.11')
        host13 = self.addHost('CVRC', cls=Host, ip='10.0.0.14')
        host14 = self.addHost('PMU1', cls=Host, ip='10.0.0.13')
        

        switch1 = self.addSwitch('s1', cls=OVSKernelSwitch, ip='10.0.0.22')
        switch2 = self.addSwitch('s2', cls=OVSKernelSwitch, ip='10.0.0.57')
        
        self.addLink(host1, switch2)
        self.addLink(host2, switch2)
        self.addLink(host3, switch2)
        self.addLink(host4, switch2)
        self.addLink(host5, switch2)
        self.addLink(host6, switch2)
        self.addLink(host7, switch2)
        self.addLink(host8, switch2)
        self.addLink(host9, switch2)
        self.addLink(host10, switch2)
        self.addLink(host11, switch1)
        self.addLink(host12, switch2)
        self.addLink(host13, switch2)
        self.addLink(host14, switch2)
        self.addLink(switch1, switch2)

topos = { 'OmnetTopo': ( lambda: MyTopo() ) }
