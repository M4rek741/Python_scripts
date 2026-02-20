#!/usr/bin/env python3.12
import json
from napalm import get_network_driver

ScrubbingCenters = {'192.168.255.155',
           '192.168.255.156'
           }

for ip_address in ScrubbingCenters:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    R1S1 = driver(ip_address, 'david', 'cisco')
    R1S1.open()
    bgp_neighbors = R1S1.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent=4))
    R1S1.close()

R1S1.close()
