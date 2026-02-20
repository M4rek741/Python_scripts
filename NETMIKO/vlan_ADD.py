#Tell what INTERPRETER should be used.
#!/usr/bin/env python3.12

#Import the ConnectHandler class
from netmiko import ConnectHandler
from pprint import pprint

#Define the devices to connect to
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

#Connect to the devices, show interfaces info + save the output.
for device in all_devices:
    net_connect = ConnectHandler(**device)

    #save the output to the file.
    with open("interfaces_output.txt", "w") as file:
        interfaces_before_output = net_connect.send_command('show ip interface brief')
        file.write(interfaces_before_output + "\n")

    #print the output to the screen.
    pprint(interfaces_before_output)

    with open("vlan_before.txt", "w") as file:
        vlan_before_output = net_connect.send_command('show vlan brief')
        file.write(output + "\n")

     #print the output to the screen.
     pprint(vlan_before_output)

     for i in range (40,50):
         print("Creating VLAN " + str(i))
         config_commands = ['vlan ' + str(i), 'name Python_VLAN ' + str(i)]
         new_vlan_output = net_connect.send_config_set(config_commands)
         print (new_vlan_output)

      #Check the VLANs number:
      interfaces_after_output = net_connect.send_command('show ip interface brief')
        pprint(interfaces_after_output)

    #disconnect from the device
    device.disconnect()
