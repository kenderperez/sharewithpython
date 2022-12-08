import scapy.all as scapy
import socket
ip = "192.168.0.103"
arp_request = scapy.ARP(pdst=ip)
broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
arp_request_broadcast = broadcast/arp_request
answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

host = {}
for element in answered_list:
	host["ip"]=element[1].psrc
	host["mac"]= element[1].hwsrc
	

print(host["ip"])
print(host["mac"])
