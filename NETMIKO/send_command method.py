#!/usr/bin/env python3.12
#Import class for the SSH connection
from netmiko import ConnectHandler
from pprint import pprint

S2 = {
	'device_type': 'cisco_ios',
	'host':'192.168.255.128',
	'username':'david',
	'password':'cisco',
	}
#Loggin to the device
net_connect = ConnectHandler(**S2)
print("Conencted Succesfully")

cmd_output = net_connect.send_command("show ip interface brief")

#Print the output to the screen
pprint(cmd_output)

#Write the output to the file
#with open("bgp_summary_output.txt", "w") as file:
#	file.write(cmd_output + "\n")

#Disconnect from the device
net_connect.disconnect()
