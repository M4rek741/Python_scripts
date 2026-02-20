#!/usr/bin/env python3.12
#Tell the system what interpreter to use.


#Import the modules youw want to call
from netmiko import ConnectHandler
from pprint import pprint

#Define a device to connect to
S2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.255.130',
	'username': 'david',
	'password': 'cisco',
	}

all_devices = [S2]

#Connect to the device with netmiko
#Two_ASTRIKSs mean UNPACKING the dictionary and pass the kye-value pairs as funtion arguments.
for device in all_devices:
	device_connect = ConnectHandler(**device)

	#Accept the connection
	pprint("Successfully connected")

	#Send the command "get facts"
	interface_output = device_connect.send_command("show ip interface brief")

	#Print the output to the screen
	pprint(interface_output)

	#Print the output to the file.txt
	#with open("show_facts_LUZNE_2.txt", "w") as file:
	#	file.write(str(interface_output))

	#disconnect the session
	device_connect.disconnect()










#Tell the system WHAT INTERPRETER should be used.
#!/usr/bin/env python3.12

# import the modules you want to call        
from netmiko import ConnectHandler
from pprint import pprint

# Define a device to connect to
S2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.255.128',
	'username': 'david',
	'password': 'cisco',
	}

all_devices = [S2]

# connect to the device with netmiko
for device in all_devices:
	device_connect = ConnectHandler(**device)

# Accept the connection
	pprint("Successfully connected")

# Send the command "show ip interface brief"
	interface_output = device_connect.send_command("show ip interface brief")

# Print the output to the screen
	pprint(interface_output)

# Print the output to the file.txt
	with open("show_interfaces_LUZNE.txt", "w") as file:
		file.write(interface_output)
