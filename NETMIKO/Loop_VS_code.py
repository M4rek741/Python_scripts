#!/usr/bin/python3

import getpass
import sys
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

for n in range(73,76):
    HOST = "192.168.122." + str(n)
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")


    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")

    for n in range(2,10):
        
        tn.write( str.encode("vlan " + str(n) + "\n") )
        tn.write( str.encode("name Python_VLAN_" + str(n) + "\n") )

    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))