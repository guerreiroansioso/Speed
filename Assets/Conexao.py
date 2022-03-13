# coding: utf-8  
# !/usr/bin/env python3

import socket, re, time
from Assets.Exibir import *

class Conexao:
    def __init__(self, ipLocal, ipExterno, porta):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.infoLocal = (ipLocal, int(porta))
        self.infoExterno = (ipExterno, int(porta))

    @staticmethod
    def Verificar(string):
        resultadoRegEx = re.findall(r'\[(.+?)\]', string)
        return resultadoRegEx

    def Apoio(self):
        self.tcp.bind(self.infoLocal)
        self.tcp.listen(1)
        conexao, externo = self.tcp.accept()
        Exibir.Correto('Recebeu conexão de ', conexao, '.')

        conteudoRecebido = (conexao.recv(64)).decode()
        if conteudoRecebido == '[TCP]':
            quantidadeTCP = 0
            while True:
                conteudoLoop = (conexao.recv(1024)).decode()
                if conteudoLoop == '[/TCP]': break
                if conteudoLoop is not None: quantidadeTCP += 1
            
            conexao.send(f'[{quantidadeTCP}]'.encode())

        time.sleep(1)
        Conexao.Close(conexao)


    def Transferir(self):
        self.tcp.connect(self.infoExterno)

        pedidoDeEnvio = '[TCP]'.encode()
        self.tcp.send(pedidoDeEnvio)

        time.sleep(1)

        iterador = 0; tempoMaximo = 20; tempoInicial = time.time()
        while True:
            Exibir.Correto('Enviando pacotes ...')
            tempoAtual = time.time()
            for variavel in range(8):
                conteudoPreparado = f'[{iterador}]'.encode()
                
                self.tcp.send(conteudoPreparado)
                iterador += 1
            tempoCorrente = tempoAtual - tempoInicial
            if tempoCorrente >= tempoMaximo:
                break

        self.tcp.send('[/TCP]'.encode())

        time.sleep(1)

        retornoApoio = (self.tcp.recv(64)).decode()
        retornoSeparado = Conexao.Verificar(retornoApoio)
        Exibir.Correto('Último pacote enviado: ', retornoSeparado)

        Conexao.Close(self.tcp)
        
    @staticmethod
    def Close(socket):
        socket.close()