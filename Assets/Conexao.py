# coding: utf-8  
# !/usr/bin/env python3

from ast import BitAnd
import socket, re, time
from Assets.Calculo import Calculo
from Assets.Exibir import *
from Assets.Perguntas import Perguntas

class Conexao:
    def __init__(self, ipLocal, ipExterno, porta):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.infoLocal = (ipLocal, int(porta))
        self.infoExterno = (ipExterno, int(porta))
        self.udpLocal = (ipLocal, int(porta) +1)
        self.udpExterno = (ipExterno, int(porta) + 1)

    @staticmethod
    def Verificar(string):
        resultadoRegEx = re.findall(r'\[(.+?)\]', string)
        return resultadoRegEx

    def ReceberTCP(self):
        quantidadeTCP = 0
        while True:
            conteudoLoop = (self.conexao.recv(500)).decode()
            #print()
            #print(conteudoLoop)
            conteudoFiltrado = Conexao.Verificar(conteudoLoop)
            #print(conteudoFiltrado)
            if len(conteudoFiltrado) == 1:
                if conteudoFiltrado[0] == '/TCP': break
            if conteudoLoop is not None: quantidadeTCP += 1
        
        self.conexao.send(f'[{quantidadeTCP}]'.encode())

    def ReceberUDP(self):
        pass

    def EnviarTCP(self, tempoMaximo):
        iterador = 0; tempoInicial = time.time()
        while True:
            tempoAtual = time.time()
            for variavel in range(8):
                conteudoPreparado = 'teste de rede *2022*'.encode()
                
                self.tcp.send(conteudoPreparado)
                iterador += 1
            tempoCorrente = tempoAtual - tempoInicial
            if tempoCorrente >= tempoMaximo: break

        self.tcp.send('[/TCP]'.encode())
        return iterador

    def EnviarUDP(self, tempoMaximo):
        pass

    def Apoio(self):
        self.tcp.bind(self.infoLocal)
        self.tcp.listen(1)

        self.conexao, externo = self.tcp.accept()
        Exibir.Correto('Recebeu conexão de ', self.conexao, '.')

        conteudoRecebido = (self.conexao.recv(500)).decode()
        if conteudoRecebido == '[TCP]':
            self.ReceberTCP()
        
        if conteudoRecebido == '[UDP]':
            self.ReceberUDP()

        time.sleep(1)


    def Transferir(self, tempoMaximo):
        self.tcp.connect(self.infoExterno)

        respostaProtocolo = Perguntas.ProtocoloUsado()
        if respostaProtocolo == 1:
            pedidoDeEnvio = '[TCP]'.encode()
            self.tcp.send(pedidoDeEnvio)

            Exibir.Simples('Enviando pacotes TCP...')
            qtdEnviados = self.EnviarTCP(tempoMaximo)
        elif respostaProtocolo == 2:
            pedidoDeEnvio = '[UDP]'.encode()
            self.tcp.send(pedidoDeEnvio)

            Exibir.Simples('Enviando pacotes UDP...')
            self.EnviarUDP(tempoMaximo)

        retornoApoio = (self.tcp.recv(500)).decode()
        retornoSeparado = Conexao.Verificar(retornoApoio)
        qtdRecebidos = int(retornoSeparado[0])

        Exibir.Correto('Foram enviados ', Calculo.ColocarPontuacao(qtdRecebidos * 500), ' no total.')
        Exibir.Errado('Foram perdidos ', Calculo.ColocarPontuacao(qtdEnviados - qtdRecebidos), ' pacotes.')

        pacotesRecebidosSeg = Calculo.PacotesPorSeg(int(qtdRecebidos), 5)
        bitsRecebidosSeg = Calculo.BitsPorSeg(int(qtdRecebidos), 5, 64)
        megabitsRecebidosSeg = Calculo.MegaPorSeg(bitsRecebidosSeg)
        Exibir.Simples('Foram enviados ', Calculo.ColocarPontuacao(pacotesRecebidosSeg), ' pacotes/s.')
        Exibir.Simples('Foram enviados ', Calculo.ColocarPontuacao(bitsRecebidosSeg), ' bits/s.')
        Exibir.Simples('Equivalente à ', Calculo.ColocarPontuacao(megabitsRecebidosSeg), ' Mbits/s.')
        

        #Conexao.Close(self.tcp)
        
    @staticmethod
    def Close(socket):
        socket.close()