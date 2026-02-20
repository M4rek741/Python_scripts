#Tell the system WHAT INTERPRETER should be used.
#!/usr/bin/env python3.12
#For readable ('pretty printed') format.
import json
#For better text visibility
from textwrap import indent

#reports commands for a specific device (Cisco,Juniper etc.)
from napalm import get_network_driver
# Step 1: Get the class for IOS
driver = get_network_driver('ios')
# Step 2: Create an instance of the driver
S2 = driver(
    hostname='192.168.255.128', 
    username='david', 
    password='cisco'
    )

#connect to the device
S2.open() 

#Retrives device information
facts = S2.get_facts()

#Save to the file in a recommended way.
with open("output_get_facts.txt", "w") as file:
    json.dump(facts, file, indent=4)
    file.write("\n")

S2.close()