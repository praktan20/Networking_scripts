from netadder import *
import nmap

def FindHost(network):
	ipNet = IPNetwork(network)
	hosts = list(ipNet)
	if hosts > 2:
		hosts.remove(ipNet.broadcast)
		hosts.remove(ipNet.network)
	hostlist = [str(hosts) for host in hosts]
	return hostlist
host = FindHost(network)
network = '192.168.0.0/24'
print host
