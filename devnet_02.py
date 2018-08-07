#!/usr/bin/python
import getpass
import sys
import telnetlib

HOST = "192.168.126.11"
user = raw_input("Digite seu usuario Telnet: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("vlan 10\n")
tn.write("name devnet10\n")
tn.write("vlan 20\n")
tn.write("name devnet20\n")
tn.write("vlan 30\n")
tn.write("name devnet30\n")
tn.write("conf t\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
