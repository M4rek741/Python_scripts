#Hash with excamation mark inform us 
#which interpreter should be used.
#!/usr/bin/env python3.12

import getpass
import telnetlib

HOST = "192.168.255.247"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write((user + "\n").encode('utf-8'))
if password:
    tn.read_until(b"Password: ")
    tn.write((password + "\n").encode('utf-8'))

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")

for n in range(2,10):
    tn.write(("vlan " + str(n) + "\n").encode('ascii'))
    tn.write(("name Python_VLAN_" + str(n) + "\n").encode('ascii'))


tn.write(b"end\n")
tn.write(b"exit\n")

print (tn.read_all())