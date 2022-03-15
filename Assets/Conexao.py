# coding: utf-8  
# !/usr/bin/env python3

import socket, re, time
from Assets.Exibir import *
from Assets.Perguntas import Perguntas

class Conexao:
    def __init__(self, ipLocal, ipExterno, porta):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.infoLocal = (ipLocal, int(porta))
        self.infoExterno = (ipExterno, int(porta))
        self.udpLocal = (ipLocal, int(porta) +1)
        self.udpExterno = (ipExterno, int(porta) + 1)

    @staticmethod
    def Verificar(string):
        resultadoRegEx = re.findall(r'\[(.+?)\]', string)
        return resultadoRegEx

    def RedirecionarTCP(self):
        quantidadeTCP = 0
        while True:
            conteudoLoop = (self.conexao.recv(64)).decode()
            if conteudoLoop == '[/TCP]': break
            if conteudoLoop is not None: quantidadeTCP += 1
        
        self.conexao.send(f'[{quantidadeTCP}]'.encode())

    def RedirecionarUDP(self):
        quantidadeUDP = 0
        while True:
            conteudoLoop, cliente = self.udp.recvfrom(64)
            if conteudoLoop == '[/UDP]': break
            if conteudoLoop is not None: quantidadeUDP += 1
            
        self.conexao.send(f'[{quantidadeUDP}]'.encode())

    def EnviarTCP(self, tempoMaximo):
        iterador = 0; tempoInicial = time.time()
        while True:
            tempoAtual = time.time()
            for variavel in range(8):
                conteudoPreparado = f'[{iterador}]'.encode()
                
                self.tcp.send(conteudoPreparado)
                iterador += 1
            tempoCorrente = tempoAtual - tempoInicial
            if tempoCorrente >= tempoMaximo:
                break

        self.tcp.send('[/TCP]'.encode())

    def EnviarUDP(self, tempoMaximo):
        iterador = 0; tempoInicial = time.time()
        while True:
            tempoAtual = time.time()
            for variavel in range(8):
                conteudoPreparado = f'[{iterador}]'.encode()
                
                self.udp.sendto(conteudoPreparado, self.udpExterno)
                iterador += 1
            tempoCorrente = tempoAtual - tempoInicial
            if tempoCorrente >= tempoMaximo:
                break

        self.tcp.send('[/UDP]'.encode())

    def Apoio(self):
        self.tcp.bind(self.infoLocal)
        self.tcp.listen(1)
        self.udp.bind(self.udpLocal)

        
        self.conexao, externo = self.tcp.accept()
        Exibir.Correto('Recebeu conexão de ', self.conexao, '.')

        conteudoRecebido = (self.conexao.recv(64)).decode()
        if conteudoRecebido == '[TCP]':
            self.RedirecionarTCP()
        
        if conteudoRecebido == '[UDP]':
            self.RedirecionarUDP()

        time.sleep(1)
        #Conexao.Close(conexao)


    def Transferir(self):
        self.tcp.connect(self.infoExterno)

        respostaProtocolo = Perguntas.ProtocoloUsado()
        if respostaProtocolo == 1:
            pedidoDeEnvio = '[TCP]'.encode()
            self.tcp.send(pedidoDeEnvio)

            time.sleep(1)

            Exibir.Simples('Enviando pacotes TCP...')
            self.EnviarTCP(5)
        elif respostaProtocolo == 2:
            pedidoDeEnvio = '[UDP]'.encode()
            self.tcp.send(pedidoDeEnvio)

            time.sleep(1)

            Exibir.Simples('Enviando pacotes UDP...')
            self.EnviarUDP(5)

        

        retornoApoio = (self.tcp.recv(64)).decode()
        retornoSeparado = Conexao.Verificar(retornoApoio)
        Exibir.Simples('Último pacote enviado: ', retornoSeparado)
        

        #Conexao.Close(self.tcp)
        
    @staticmethod
    def Close(socket):
        socket.close()