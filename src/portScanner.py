try:
   from scapy.all import *
except ImportError:
   raise ImportError('scapy is not installed, please install it by running: '
          'pip install scapy')


ports = [21, 22,2,80, 443, 8080, 5000]

packIp = IP(dst  = "Ip: ")
packTCP = TCP(dport=ports, flasgs="S")
pack = packIP/packTCP

ans, unans = sr(pack, inter=0.1, timeout=1)
print("Port/State")
for packReceived in ans:

    print(packReceved[1][IP].sport, "\t", packReceived[1][TCP].sprintf("%flags"))