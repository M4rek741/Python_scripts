#Tell the system WHAT INTERPRETER should be used.
#!/usr/bin/env python3.12
#For readable ('pretty printed') format.

#logging module provides a tool to create log messages from Python programs.
import logging
from logging import config
from math import exp
from textwrap import indent

#From netmiko library import the ConnectHandler class
#ConnectHandler 
from netmiko import ConnectHandler

# Create an instance
S2 = {
    'host' : '192.168.255.128', 
    'username' : 'david', 
    'password' : 'cisco',
    'device_type' : 'cisco_ios',
    }

#Commands to be run on the device
copy_cmd = 'copy running-config startup-config'
copy_cmd_e = 'Destination filename'

cmd_list = [[copy_cmd, copy_cmd_e],
            ['\n', "Do you want to over write"],
            ['\n', ''r'#']]

net_connect = ConnectHandler(**S2)
print("connected successfully")

cmd_output = net_connect.send_multiple_command(cmd_list, read_timeout=50)
print(cmd_output)


#config = net_connect.send_config_set(Commands)
#print(config)
#print(net_connect.send_command('show ip interface brief'))
