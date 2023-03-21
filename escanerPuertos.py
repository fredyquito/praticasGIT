#!/usr/bin/python
import  socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("[*] ingresa la IP del host")

def escanerPuertos(port):
        if sock.connect_ex(host,port):
                print(colored("pueerto %d esta cerrado" % (port),"red"))
        else:
                print(colored("pueerto %d esta abierto" % (port),"green"))
for port in range(1,1000):
        escanerPuertos(port)