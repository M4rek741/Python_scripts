#!/usr/bin/env python3.12

from netmiko import ConnectHandler

S1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.155',
    'username': 'david',
    'password': 'cisco',
    }

S2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.156',
    'username': 'david',
    'password': 'cisco',
    }

S3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.157',
    'username': 'david',
    'password': 'cisco',
    }

with open('iosv_l2_config') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [S1, S2, S3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)