#Tell what interpreter to use
#!/usr/bin/env python3.12
import json
#reports commands for a specific device (Cisco,Juniper etc.)
from napalm import get_network_driver
# Step 1: Get the class for IOS
driver = get_network_driver('ios')
# Step 2: Create an instance of the driver
S1 = driver('192.168.255.128', 'david', 'cisco')

S1.open()
print("Connected successfully to the device")

mac_output = S1.get_mac_address_table()
print (json.dumps(mac_output, indent=4))
with open("output_mac_address.txt", "w") as file:
    json.dump(mac_output, file, indent=4)
    file.write("\n")

interfaces_output = S1.get_interfaces()
print (json.dumps(interfaces_output, sort_keys=True, indent=4))
with open("output_interfaces.txt", "w") as file:
    json.dump(interfaces_output, file, indent=4)
    file.write("\n")

counters_output = S1.get_interfaces_counters()
print (json.dumps(counters_output, sort_keys=True, indent=4))
with open("output_counters.txt", "w") as file:
    json.dump(interfaces_output, file, indent=4)
    file.write("\n")

ping_output = S1.ping(8.8.8.8)
print (json.dumps(ping_output, sort_keys=True, indent=4))
with open("ping_output.txt", "w") as file:
    json.dump(ping_output, file, indent=4)
    file.write("\n")

S1.close()
print("Connection closed.")