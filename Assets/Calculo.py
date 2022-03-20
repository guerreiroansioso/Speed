# coding: utf-8  
# !/usr/bin/env python3

class Calculo:
    @staticmethod
    def PacotesPorSeg(pacotes, segundos):
        return pacotes / segundos

    @staticmethod
    def BitsPorSeg(pacotes, segundos, recvSize):
        QtdSegundo = Calculo.PacotesPorSeg(pacotes, segundos)
        return QtdSegundo * recvSize

    @staticmethod
    def MegaPorSeg(bitsPorSeg):
        return bitsPorSeg / 1048576

    @staticmethod
    def ColocarPontuacao(valorOriginal):
        return (f'{valorOriginal:_.2f}').replace('.', ',').replace('_', '.')