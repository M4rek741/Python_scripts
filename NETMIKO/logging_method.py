#Tell the system WHAT INTERPRETER should be used.
#!/usr/bin/env python3.12
#For readable ('pretty printed') format.
from fileinput import filename
import json

#logging module provides a tool to create log messages from Python programs.
import logging
from logging import config
from math import log
from venv import logger

#Ennable logging at the DEBUG level
logging.basicConfig(filename="demo_netmiko.log", level=logging.DEBUG)
#Create a logger object called 'netmiko'
logger =logging.getLogger("netmiko")

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

net_connect = Netmiko(**S2)
logger.info("Connection established to %s", S2['host'])
print("connected successfully")

show_cmd = (net_connect.send_command('show ip interface brief'))

#This opens (or creates) a text file named demo_netmiko.log in write mode ('w').
with open("demo_netmiko.log", 'w') as file:
    logger.info("Writing log to a file")
    file.write(show_cmd)