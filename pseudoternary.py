import numpy as np

#PSEUDOTERNARY
def PSEUDOTERNARY(dados):
    pseudoternary = []
    ultimo_volt = -1
    for i in range (len(dados)):
        if dados[i] == 1:
            pseudoternary.append(0)
        else:
            ultimo_volt *= -1
            pseudoternary.append(ultimo_volt)
    return pseudoternary