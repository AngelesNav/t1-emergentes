from mininet.net import Mininet
from mininet.node import Controller
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def chile_australia_topology():
    # Crear la red con controlador
    net = Mininet(controller=Controller, link=TCLink)
    net.addController('c0')

    # Crear hosts
    hostChile = net.addHost('h1')
    hostAustralia = net.addHost('h2')

    # Crear switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    # Crear enlaces con los parámetros especificados
    net.addLink(s1, s2, cls=TCLink, bw=1000, delay='30ms', loss=5)  # Ancho de banda ajustado a 1000 Mbps
    net.addLink(s2, s3, cls=TCLink, bw=500, delay='20ms', loss=2)
    net.addLink(s3, s4, cls=TCLink, bw=1000, delay='40ms', loss=3)  # Ancho de banda ajustado a 1000 Mbps
    net.addLink(s1, hostChile)
    net.addLink(s4, hostAustralia)

    # Iniciar la red
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    chile_australia_topology()