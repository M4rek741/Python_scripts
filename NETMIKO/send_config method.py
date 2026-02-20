#!/usr/bin/env python3.12
#Import class for the SSH connection
from token import OP
from netmiko import ConnectHandler

S2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.255.128',
	'username': 'david',
	'password': 'cisco',
	}
commands = [
	'int gig0/0',
	'no switchport',
	'ip address 10.10.10.1 255.255.255.252',
	'no shut',
	'exit'
]

#Loggin to the device
net_connect = ConnectHandler(**S2)
print("Connnected Succesfully")

#Disable paging
net_connect.send_command("terminal length 0")

#Configure method
interface_configuration = net_connect.send_config_set(commands)
print(interface_configuration)

#Show method
show_output = net_connect.send_command("show ip interface brief")
print(show_output)

#Write the output to the file
with open("interface_brief_output.txt", "w") as file:
	file.write(show_output + "\n")

#terminate the session
net_connect.disconnect()
print("Disconnected Succesfully")













#NETMIKO
#!/usr/bin/env python3.12
from netmiko import ConnectHandler

S2 = {
	'device_type': 'cisco_ios',
	'host':'192.168.255.128',
	'username':'david',
	'password':'cisco',
	}

net_connect = ConnectHandler(**S2)
print("Conencted Succesfully")

#Disable paging
net_connect.send_command("terminal length 0")

#send_command method -> send one command to the device
cmd_output = net_connect.send_command("show ip interface brief")
print(cmd_output)

#Write the output to the file
with open ("interface_brief_output.txt", "w") as file:
	file.write(cmd_output + "\n")

#terminate the session
net_connect.disconnect()