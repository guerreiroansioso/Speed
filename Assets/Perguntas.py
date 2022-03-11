# coding: utf-8  
# !/usr/bin/env python3

from Assets.Msg import *


def Perguntas_InfoConexao():
    ipLocal = Msg_Input('Qual é o seu ip local?')
    ipExterno = Msg_Input('Qual é o seu ip externo?')
    porta = Msg_Input('Qual é o porta utilizado?')

    Msg_Barramento('Info:')

    Msg_Correto('Ip local:', ipLocal)
    Msg_Correto('Ip externo:', ipExterno)
    Msg_Correto('Porta:', porta)

    Msg_Input()

    Msg_Alerta('Tchau!', 'Até logo!')

    return ipLocal, ipExterno, porta

def Perguntas_Modo():
    pass

def Perguntas_Repetir():
    pass