import numpy as np

#MANCHESTER
def MANCHESTER(dados):
    manchester = []
    for i in range(len(dados)):
      if dados[i] == 0:
        manchester.append(1)
        manchester.append(-1)
      else:
        manchester.append(-1)
        manchester.append(1) 
    return manchester