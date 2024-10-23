#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import os
import pickle
import time
import socket
import signal

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# User and group IDs for root and a specific level user
uid_root = os.getuid()  # Assuming the script is started with root privileges
gid_root = os.getgid()
uid_level17 = 1080  # Example UID for a non-privileged user
gid_level17 = 1080  # Example GID for a non-privileged group

def server(skt):
    line = skt.recv(1024)

    obj = pickle.loads(line)

    for i in obj:
        skt.send(("why did you send me " + i + "?\n").encode())

# Drop privileges
def drop_privileges():
    try:
        os.setegid(gid_level17)
        os.seteuid(uid_level17)
        print("Privileges dropped to UID - GID : ")
        print(uid_level17)
        print(gid_level17)
    except OSError:
        print("Failed to drop privileges.")
        exit(1)

# Restore privileges
def restore_privileges():
    try:
        os.seteuid(uid_root)
        os.setegid(gid_root)
        print("Privileges restored to UID - GID :")
        print(uid_root)
        print(gid_root)
    except OSError:
        print("Failed to restore privileges.")
        exit(1)

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
skt.bind(('0.0.0.0', 10008))
skt.listen(10)

while True:
    clnt, addr = skt.accept()

    if os.fork() == 0:
        clnt.send("Accepted connection from %s:%d" % (addr[0], addr[1])) 
        drop_privileges()  # Drop privileges before processing
        server(clnt)
        restore_privileges()  # Restore privileges before exiting the child process
        exit(1)
