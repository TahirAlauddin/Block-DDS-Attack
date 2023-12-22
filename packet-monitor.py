from collections import Counter
from scapy.all import sniff, TCP, IP
import os

counter = Counter()

ip_addresses = {}
command_to_block_ip = "netsh advfirewall firewall add rule name=\"Block IP {ipaddress}\" dir=in action=block remoteip={ipaddress}"

def block_ip(pkt):
    global ip_addresses
    src = pkt[IP].src
    counter.setdefault(src, 0)
    counter.update({src: counter.get(src)+1})
    ip_addresses[src] 
    if TCP in pkt and ip_addresses[src]:
        print("Blocking packet from IP address: 1.2.3.4")
        # os.system(command_to_block_ip)
        return
    else:
        pkt.show()

## Setup sniff, filtering for IP traffic
sniff(filter="tcp", prn=block_ip)


# netsh advfirewall firewall add rule name="Block IP on Port 1112" dir=in action=block protocol=TCP localport=1112 remoteip=127.0.0.1
