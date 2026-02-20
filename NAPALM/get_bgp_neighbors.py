#!/usr/bin/env python3.12
import json
from logging import config
from napalm import get_network_driver
driver = get_network_driver('ios')
S1 = driver('192.168.255.155', 'david', 'cisco')
S1.open()

ios_output = S1.get_facts()

bgp_neighbors =S1.get_bgp_neighbors()
print (json.dumps(bgp_neighbors, indent=4))

S1.close()



