#!/usr/bin/env python3.12

from logging import config
from netmiko import ConnectHandler

S1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.127',
    'username': 'david',
    'password': 'cisco',
    }

S2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.128',
    'username': 'david',
    'password': 'cisco',
    }

all_devices = [S2]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show ip int brief')
    print (output)

    with open("vlan_creation_output.txt", "w") as file:
        file.write(output + "\n")

    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show vlan brief')
    print (output)

    for i in range (2,10):
        print ("Creating VLAN " + str(i))
        config_commands = ['vlan ' + str(i), 'name Python_VLAN ' + str(i)]
        output = net_connect.send_config_set(config_commands)
        print (output)

    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show vlan brief')
    print (output)