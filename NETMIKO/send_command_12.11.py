    #Script plan
    #1 connect to multiple devices
    #2 Accept the connection
    #3 Send the command 'show ip interface brief'
    #4 Print the output to the screen
    #5 Print the output to the file.txt
    #6 Configure the loopback interface on each device
    #7 Configure vlans on each switch
    #8 Disconnect from the device

#Tell the system WHAT INTERPRETER should be used.
#!/usr/bin/env python3.12

#More readable output
from pprint import pprint

#Establish a connection to a network device.
from netmiko import ConnectHandler


S2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.128',
    'username': 'david',
    'password': 'cisco',
    }

all_devices = [S2]

#1. Connect to multiple devices
for device in all_devices:
    device_connect = ConnectHandler(**device)

#2. Accept the connection.
    pprint("Succesfully Connected")

#3.Send the command "Show IP interface brief"
    interface_output = device_connect.send_command("show ip interface brief")

#4.Print the output to the screen.
    pprint(interface_output)

#5.Print the output to the file.txt
    with open("show_interfaces_12.11.txt", "w") as file:
                file.write(interface_output)

#6.Configure the loopback interface on each device
for i in range(1,10):
    Loopback_Commands = [
                     'interface loopback 200' + str(i),
                     'description Configured by Netmiko Script',
                     'ip address 11.' + str(i) + '.' + str(i) + '.1 255.255.255.0',
                     'no shutdown'
                     ]
    print ("Creating loopback 200" + str(i))
    loopback_output = device_connect.send_config_set(Loopback_Commands)
    pprint(loopback_output)

pprint(device_connect.send_command("show ip interface brief"))

#7. Configure vlans on each switch
for i in range(1,10):
    vlan_id = 30 + i
    pprint("Creating vlan " + str(vlan_id))
    
    Vlan_Commands = [
        'vlan ' + str(30 + i),
        'name Python_VLAN ' + str(vlan_id),
        ]
    vlan_output = device_connect.send_config_set(Vlan_Commands)
    pprint(vlan_output)

#9. Print the vlan configuration to verify
pprint(device_connect.send_command("show vlan brief"))

#9. Disconnect from the device
device_connect.disconnect()














#Tell which interpreter to use
#!/usr/bin/env python3.12

#More readable output
from pprint import pprint
#Establish a connection to a network device.
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

all_devices = [S1,S2]

for device in all_devices:
    #Connect to the device
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show ip interface brief')
    pprint(output + "\n")
   # with open("netmiko_show_interfaces_output.txt", "w") as file:
   #     file.write(output + "\n")

    #Disconnect from the device
    net_connect.disconnect()

  