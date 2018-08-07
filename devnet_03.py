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


tn.write("\n")
tn.write("conf t\n")

for i in range (2,10)
    tn.write("vlan \n" +(i) "\n" )


tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
