#Tell the system WHAT INTERPRETER should be used.
#!/usr/bin/env python3.12
#For readable ('pretty printed') format.
import json
#For better text visibility
from logging import config
from os import device_encoding
from textwrap import indent

#reports commands for a specific device (Cisco,Juniper etc.)
from napalm import get_network_driver
# Step 1: Get the class for IOS
driver = get_network_driver('ios')
# Step 2: Create an instance of the driver
S2 = driver(
    hostname='192.168.255.128', 
    username='david', 
    password='cisco')

#connects to the device
S2.open() 
print("Connected Successfully")

S2.load_merge_candidate(config='interface loopback1003\n ip address 2.1.1.1 255.255.255.255')

print(S2.compare_config())
if len(S2.compare_config()) > 0:
    choice = input("Apply changes? [y/n]: ")
    if choice == 'y':
        S2.commit_config()
        print("Changes applied.")
    else:
        print("Changes discarded.")
        S2.discard_config()
S2.close()
print("Disconnected from the device")

#Save the information to the file
facts = S2.get_facts()
open("output.txt", "w").write(json.dumps(facts, indent=4) + "\n")
