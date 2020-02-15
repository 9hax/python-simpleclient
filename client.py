#!/usr/bin/env python

import socket
try:
    from config import *
except:
    HOST = str(input("Host? >"))
    PORT = int(input("Port? >"))

BUFFER_SIZE = 4096

mesg = "HELLO CLIENT"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while mesg!="exit":
    mesg = input("Message? >")
    s.send(bytes(mesg, "utf-8"))
    data = s.recv(BUFFER_SIZE)
    print("received data:"+str(data))
s.close()
