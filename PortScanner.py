#!/usr/bin/python3
import socket, sys
import informacoes
from datetime import datetime

inicio = datetime.now()

def port_scan():
    if len(sys.argv) <= 1:
        print("\033[1;31;31mERRO:\033[m Argumentos insuficientes...")
        print("\033[1;36;36mUSAGE:\033[m python escript.py [IP]")
    else:
        lista_portas = informacoes.escolher_listaPortas() 
        print("\n\033[4;36;36mPortScan no ALVO:\033[m", sys.argv[1])
        print("\033[4;36;36mA lista escolhida possui as seguintes portas:\033[m\n", lista_portas, "\n")
        for porta in lista_portas:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #socket.setdefaulttimeout(0.5)
            if (sock.connect_ex((sys.argv[1], porta)) == 0):
                print("\033[1;0;31m[+] Porta TCP Aberta:\033[m", porta)
                if (porta == 21 or porta == 22):
                    banner = sock.recv(1024)
                    print("\033[1;0;32m[+] BANNER:\033[m", banner)
                    sock.close()

    final = datetime.now()
    tempo_total = (final - inicio)
    print("\n\033[1;0;32mO tempo de duracao do scan foi de:\033[m", tempo_total)
port_scan()
