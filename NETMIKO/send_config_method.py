#Tell the system WHAT INTERPRETER should be used.
#!/usr/bin/env python3.12
#For readable ('pretty printed') format.
import json
#For better text visibility
from logging import config
from textwrap import indent

#From netmiko library import the Netmiko class
from netmiko import Netmiko

# Create an instance
S2 = {
    'host' : '192.168.255.128', 
    'username' : 'david', 
    'password' : 'cisco',
    'device_type' : 'cisco_ios',
    }

#Commands to be run on the device
Commands = [f'interface loopback1001',
            f'description Configured by Netmiko',
            f'ip address 11.1.1.0 255.255.255.255',
            f'no shutdown'
            ]
net_connect = Netmiko(**S2)
print("connected successfully")

for i in range (1010,1020):
    print ("Creating loopback " + str(i))
    output = net_connect.send_config_set(config_commands)
    print (output)

config = net_connect.send_config_set(Commands)
print(config)
print(net_connect.send_command('show ip interface brief'))
