#!/usr/bin/python
import getpass
import sys
import telnetlib
import time
import os

#capturar usuario e  senha
user = raw_input("Digite seu usuario Telnet: ")
password = getpass.getpass()

#determinar arquivo com equipamentos
variavel_lista = open('arquivo_equipamentos')

#capturar a data
datahoje = time.strftime("%Y%m%d")

#criando diretorio
os.mkdir(datahoje, 0755)

print ("*******************************************************\n")
print ("Criando diretorio: " +datahoje)
print ("*******************************************************\n")


comando_mover = "mv BKP-Switch-* "+datahoje

for linha in variavel_lista:
    print ("*******************************************************\n")
    print ("Salvando configuracoes do equipamento: " +linha)
    print ("*******************************************************")
    HOST = linha.strip()
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")


    tn.write("terminal length 0\n")
    tn.write("show run\n")
    tn.write("exit\n")

    ler_saida = tn.read_all()
    criar_arquivo = open("BKP-Switch-"+datahoje+"-"+HOST,"w")
    criar_arquivo.write(ler_saida)
    criar_arquivo.close

    os.system(comando_mover)

    print tn.read_all()
