#!/usr/bin/env python3

import socket

# cria um socket TCP, AF_INET usa ipv4 e SOCK_STREAM para TCP
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binda o socket no endereço
socket.bind(("localhost", 9473))
# coloca o socket em listening
socket.listen()

# espera um cliente conectar
conn, addr = socket.accept()

while True:
    data = conn.recv(1024) # recebe dados do cliente, até 1024kbs
    if not data:
        break
    print("Nova mensagem do host %s: %s" % (addr, data.decode()))

# fecha conexão e libera recursos
conn.close()
