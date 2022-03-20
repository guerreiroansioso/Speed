# coding: utf-8  
# !/usr/bin/env python3

from Assets.Conexao import *
from Assets.Exibir import *
from Assets.Perguntas import *

ipLocal, ipExterno, porta = Perguntas.Conexao()

conexao = Conexao(ipLocal, ipExterno, porta)
modoEscolhido = Perguntas.Modo()

if modoEscolhido == 1: conexao.Transferir(20)
elif modoEscolhido == 2: conexao.Apoio()

Exibir.Enter('sair!')