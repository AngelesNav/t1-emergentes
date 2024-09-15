from mininet.net import Mininet
from mininet.node import Controller
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def custom_topology():
    # Crear la red
    net = Mininet(controller=Controller, link=TCLink)

    # Agregar el controlador
    net.addController('c0')

    # Agregar hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')

    # Agregar switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    # Crear enlaces entre switches con los parámetros especificados
    net.addLink(s2, s3, bw=512, delay='6ms', loss=4)
    net.addLink(s3, s4, bw=256, delay='25ms', loss=3)

    # Crear enlaces entre switches y hosts
    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s3, h3)
    net.addLink(s4, h4)

    # Crear enlaces entre switches adicionales
    net.addLink(s1, s2)

    # Iniciar la red
    net.start()

    # Abrir la CLI de Mininet
    CLI(net)

    # Detener la red
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    custom_topology()