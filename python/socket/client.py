#!/usr/bin/env python3

import socket

# cria o socket com ipv4 e TCP
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tenta conectar, só funciona se o outro socket estiver escutando
socket.connect(("localhost", 9473))

while True:
    msg = input("Digite aqui a sua mensagem: ")
    # transforma a string em bytes e envia
    socket.send(msg.encode())