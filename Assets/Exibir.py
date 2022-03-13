# coding: utf-8  
# !/usr/bin/env python3

class Exibir:
    @staticmethod
    def Simples(*mensagens):
        print(f'\033[1;35m | \033[0;0m', end = '')
        print(*mensagens, sep = '', end = '')
        print()

    @staticmethod
    def Resetar():
        print('\033[0;0m')

    @staticmethod
    def Input(*mensagens):
        if len(mensagens) > 0: print(f'\033[1;33m | \033[0;0m', end = '')
        print(*mensagens, sep = '', end = '')
        if len(mensagens) > 0: print()
        print(' \033[1;35m>>> \033[1;33m', end = '')
        recebido = input()
        print('\033[0;0m', end = '')

        return recebido

    @staticmethod
    def Enter(*mensagens):
        print('\033[1;35m [ \033[0;0mAperte \033[1;33m"ENTER"\033[0;0m para ', end = '')
        print(*mensagens, sep = '', end = '')
        print('\033[1;35m ] \033[0;0m', end = '')
        input()

    @staticmethod
    def Correto(*mensagens):
        print(f'\033[1;92m | \033[0;0m', end = '')
        print(*mensagens, sep = '', end = '')
        print()

    @staticmethod
    def Errado(*mensagens):
        print(f'\033[1;91m | \033[0;0m', end = '')
        print(*mensagens, sep = '', end = '')
        print()

    @staticmethod
    def Alerta(*mensagens):
        print(f'\033[1;91m >>> \033[1;95m', end = '')
        print(*mensagens, sep = '', end = '')
        print('\033[1;91m <<<\033[0;0m')

    @staticmethod
    def Apagar():
        print(f'\033[A                                                              \033[A')