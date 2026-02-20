import getpass
import telnetlib

HOST = "192.168.255.246"
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
tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print (tn.read_all())
