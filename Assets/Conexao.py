# coding: utf-8  
# !/usr/bin/env python3

import socket

def Conexao_Criar(modo):
    if modo == 'utp': tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)