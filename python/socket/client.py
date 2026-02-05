#!/usr/bin/env python3

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("localhost", 9473))

while True:
    msg = input("Digite aqui a sua mensagem: ")
    socket.send(msg.encode())