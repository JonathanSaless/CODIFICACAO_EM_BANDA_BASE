import numpy as np

def PSEUDOTERNARY(dados):
  pseudoternary = []
  ultimo_volt = -1
  for i in range (len(dados)):
    if dados[i] == 0:
      ultimo_volt *= -1
      pseudoternary.append(ultimo_volt)
    else:
      pseudoternary.append(0)
  return pseudoternary
