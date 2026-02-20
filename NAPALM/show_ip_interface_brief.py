#!/usr/bin/env python3.12
#For better formatting
import json 
from textwrap import indent
from napalm import get_network_driver

driver = get_network_driver('ios')
S2 = driver(
    hostname='192.168.255.128',
    username='david',
    password='cisco',
)

S2.open()
#get device facts
facts = S2.cli(["show ip interface brief"])

#write the facts to a file in a readable JSON format.
with open("output.txt", "w") as file:
    json.dump(facts, file, indent=4)
    file.write("/n")

S2.close()