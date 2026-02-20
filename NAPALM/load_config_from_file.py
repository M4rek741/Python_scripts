#!/usr/bin/env python3.12
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
S1 = driver('192.168.255.155', 'david', 'cisco')
S1.open()

print ('Accessing 192.168.255.155')
S1.load_merge_candidate(filename='ACL.cfg')

diffs = S1.compare_config()
if len(diffs) > 0:
    print(diffs)
    S1.commit_config()
else:
    print('No changes required')
    S1.discard_config()

S1.close()