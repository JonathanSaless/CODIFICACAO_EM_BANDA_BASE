import numpy as np

def B8ZS(dados):
  b8zs = []
  ultimo_volt = -1
  cont_zeros = 1
  for i in range (len(dados)):
    if dados[i] == 1:                     #bit 1 alternância entre pulsos positivos (= +1) e negativos (= -1)
      ultimo_volt *= -1   
      b8zs.append(ultimo_volt)    
      cont_zeros = 1                      #se teve bit 1, reinicia a conta de zeros
    else:                                 #bit 0 ausência de sinal na linha (= 0), até que haja 8 zeros consecutivos
      if cont_zeros == 8:                 #quando há 8 zeros consecutivos, se último pulso positivo -> 000+-0-+, se negativo -> 000-+0+-
        b8zs[i-4] = ultimo_volt           #V mesmo sinal de ultimo pulso
        b8zs[i-3] = ultimo_volt*-1        #B sinal contrário do ultimo pulso
        #b8zs[i-2] = 0                    #já é zero, não precisa alterar
        b8zs[i-1] = ultimo_volt*-1        #V
        b8zs.append(ultimo_volt)          #B
        cont_zeros = 1    
      else:   
        b8zs.append(0)                    #se não tiver 8 zeros consecutivos, adiciona ausência de sinal na linha (= 0)
        cont_zeros +=1                    #e soma 1 no contador de zeros
  return b8zs
