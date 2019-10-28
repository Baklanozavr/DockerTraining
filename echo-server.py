#!/usr/bin/env python3

import socket

HOST = ''
PORT = 65432
LOGFILE = open('var/log/server.log', 'w')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            LOGFILE.write(data.decode('utf-8'))
            conn.sendall("OK:".encode('utf-8') + data)
