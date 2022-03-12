# coding: utf-8  
# !/usr/bin/env python3

from Assets.Exibir import *

class Perguntas:
    @staticmethod
    def Conexao():
        ipLocal = Exibir.Input('Qual é o seu ip local?')
        ipExterno = Exibir.Input('Qual é o seu ip externo?')
        porta = Exibir.Input('Qual é o porta utilizada?')

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
    def Repetir():
        pass