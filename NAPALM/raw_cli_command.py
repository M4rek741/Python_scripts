#!/usr/bin/env python3.12
import json
from textwrap import indent
from napalm import get_network_driver
driver = get_network_driver('ios')
S1 = driver('192.168.255.155', 'david', 'cisco')\

S1.open()

sh_output = S1.cli(['show ip interface brief'])

for command, output in sh_output.items():
    print(f"\n=== {command} ===")
    print(output)

S1.close()

#other option:
S1.open()
#get device facts
print("Connected successfully to the device")
facts = S1.cli(["show ip interface brief"])

print(facts["show ip interface brief"])

S1.close()