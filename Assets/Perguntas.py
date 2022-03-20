# coding: utf-8  
# !/usr/bin/env python3

from Assets.Exibir import *

class Perguntas:
    @staticmethod
    def Conexao():
        ipLocal = Exibir.Input('Informe o IP local, por favor.')
        ipExterno = Exibir.Input('Informe o IP externo, por favor.')
        porta = Exibir.Input('Informe a PORTA utilizada, por favor.')

        print()
        Exibir.Simples('Informações:')

        Exibir.Correto('Ip local:', ipLocal)
        Exibir.Correto('Ip externo:', ipExterno)
        Exibir.Correto('Porta:', porta)

        return ipLocal, ipExterno, porta
    
    @staticmethod
    def Modo():
        modoEscolhido = Exibir.Input('Testar velocidade ou servir de apoio? ( 1 - Teste, 2 - Apoio).')
        return int(modoEscolhido)

    @staticmethod
    def ProtocoloUsado():
        protocoloEscolhido = Exibir.Input('Qual protocolo será usado? ( 1 - TCP, 2 - UDP)')
        return int(protocoloEscolhido)