#!/usr/bin/env python3.12
# Tell the system what interpreter to use.

#Import the modules you want to call
from netmiko import ConnectHandler
from pprint import pprint

#Define a device to connect to
R1 = {
	'device_type': 'cisco_ios',
	'ip': '150.1.1.1',
	'username': 'david',
	'password': 'cisco',
	}
R2 = {
	'device_type': 'cisco_ios',
	'ip': '150.2.2.2',
	'username': 'david',
	'password': 'cisco',
	}
R3 = {
	'device_type': 'cisco_ios',
	'ip': '150.3.3.3',
	'username': 'david',
	'password': 'cisco',
	}
R4 = {
	'device_type': 'cisco_ios',
	'ip': '150.4.4.4',
	'username': 'david',
	'password': 'cisco',
	}

all_devices = [R1,R2,R3,R4]

#Connect to the device with netmiko
for device in all_devices:
	device_connect = ConnectHandler(**device)

	#Accept the connection
	pprint("Successfully connected")

	#Send the command "show ip bgp"
	show_bgp_summary_output = device_connect.send_command("show ip bgp summary")

	#Print the output to the screen
	pprint(show_bgp_summary_output)

	#Send the command "show ip bgp neighbors"
	show_bgp_neighbors_output = device_connect.send_command("show ip bgp neighbors | include (BGP neighbor is | Description BGP state)")

	#Print the output to the screen
	pprint(show_bgp_neighbors_output)

	#Disconnect the session
	device_connect.disconnect()