# coding: utf-8  
# !/usr/bin/env python3

import socket
from Assets.Exibir import *

class Conexao:
    def __init__(self, ipLocal, ipExterno, porta):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.infoLocal = (ipLocal, int(porta))
        self.infoExterno = (ipExterno, int(porta))

    def Apoio(self):
        self.tcp.bind(self.infoLocal)
        self.tcp.listen(1)
        conexao, externo = self.tcp.accept()
        Exibir.Correto('Recebeu conexão de ', conexao, '.')

    def Transferir(self):
        self.tcp.connect(self.infoExterno)

        pedidoDeEnvio = '[Pedido][Enviar][20]'.encode()
        self.tcp.send(pedidoDeEnvio)