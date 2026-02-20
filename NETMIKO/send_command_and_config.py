#Tell what interpreter to use
#!/usr/bin/env python3

#Tell how to handle the connectivity
from typing import final
from netmiko import ConnectHandler

#Define the device to connect to

S2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.255.128',
    'username': 'david',
    'password': 'cisco',
}

#Define the device to connect to
all_devices = [S2]

#Loop for more than one device
for device in all_devices:
    net_connect = ConnectHandler(**device)
    #Show current vlans
    current_vlan_output = net_connect.send_command('show vlan brief')
    print(current_vlan_output)

#vlan creation
for i in range(10, 21):
    print ("Creating VLAN " + str(i))
    config_commands = ['vlan ' + str(i), 'name Python VLAN ' + str(i)]
    new_vlan_output = net_connect.send_config_set(config_commands)
    print(new_vlan_output)

#Loop to verify the vlans were created
for device in all_devices:
    net_connect = ConnectHandler(**device)
    #Show new vlans
    final_vlan_output = net_connect.send_command('show vlan brief')
    print(final_vlan_output)

    #Terminate the session
    net_connect.disconnect()