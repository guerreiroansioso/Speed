# coding: utf-8  
# !/usr/bin/env python3

from cgi import print_arguments


def Msg_Resetar():
    print('\033[0;0m')

def Msg_Input(*mensagens):
    if len(mensagens) > 0: print(f'\033[1;33m | \033[0;0m', end = '')
    print(*mensagens, sep = '', end = '')
    if len(mensagens) > 0: print()
    print(' \033[1;35m>>> \033[1;33m', end = '')
    recebido = input()
    print('\033[0;0m', end = '')

    return recebido

def Msg_Enter(*mensagens):
    print('\033[1;35m [ \033[0;0mAperte \033[1;33m"ENTER"\033[0;0m para ', end = '')
    print(*mensagens, sep = '', end = '')
    print('\033[1;35m ] \033[0;0m', end = '')
    input()


def Msg_Barramento(*mensagens):
    print(f'\033[1;35m | \033[0;0m', end = '')
    print(*mensagens, sep = '', end = '')
    print()

def Msg_Correto(*mensagens):
    print(f'\033[1;92m | \033[0;0m', end = '')
    print(*mensagens, sep = '', end = '')
    print()

def Msg_Errado(*mensagens):
    print(f'\033[1;91m | \033[0;0m', end = '')
    print(*mensagens, sep = '', end = '')
    print()

def Msg_Alerta(*mensagens):
    print(f'\033[1;91m >>> \033[1;95m', end = '')
    print(*mensagens, sep = '', end = '')
    print('\033[1;91m <<<\033[0;0m')