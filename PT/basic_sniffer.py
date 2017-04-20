import socket

# Create he sniffer socket
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# Bind to localhost
sniffer.bind(('192.168.178.0', 0))

# IP header Check
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

print('sniffer is listening for incoming connections')

# Get a single packet
print(sniffer.recvfrom(65535))