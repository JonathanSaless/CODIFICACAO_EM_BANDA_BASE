import numpy as np

def B8ZS(dados):
  b8zs = []
  ultimo_volt = -1
  cont_zeros = 1
  for i in range (len(dados)):
    if dados[i] == 1:
      ultimo_volt *= -1   
      b8zs.append(ultimo_volt)    
      cont_zeros = 1
    else:
      if cont_zeros == 8:
        b8zs[i-4] = ultimo_volt
        b8zs[i-3] = ultimo_volt*-1
        b8zs[i-1] = ultimo_volt*-1
        b8zs.append(ultimo_volt)
        cont_zeros = 1    
      else:   
        b8zs.append(0)
        cont_zeros +=1
  return b8zs
