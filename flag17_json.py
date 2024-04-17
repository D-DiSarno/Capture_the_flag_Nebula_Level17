#!/usr/bin/python

import os
import json
import time
import socket
import signal

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

def server(skt):
      line = skt.recv(1024)

      obj = json.loads(line.decode())

      for i in obj:      
       clnt.send(("why did you send me " + i + "?\n").encode())
      
      clnt.send("Thank you for your data!\n".encode())
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
skt.bind(('0.0.0.0', 10009))
skt.listen(10)

while True:
      clnt, addr = skt.accept()

      if(os.fork() == 0):
          clnt.send("Accepted connection from %s:%d" % (addr[0], addr[1]))
          server(clnt)
          exit(1)
