import numpy as np

#B8ZS
def B8ZS(dados):
    b8zs = []
    ultimo_volt = -1
    cont_zeros = 1

    for i in range (len(dados)):
        if dados[i] == 1:    #quando o bit é 1 troca o sinal da voltagem
            ultimo_volt *= -1
            b8zs.append(ultimo_volt)
        else:
            if cont_zeros == 8:
                b8zs[i-4] = ultimo_volt                 #V possui mesmo sinal do ultimo volt
                b8zs[i-3] = ultimo_volt*-1              #B possui sinal contrário do ultimo volt
                #b8zs[i-2] = 0      #já é zero, então não precisa alterar
                b8zs[i-1] = ultimo_volt*-1              #V
                b8zs.append(ultimo_volt)                #B
                cont_zeros = 1
            else:
                b8zs.append(0)
                cont_zeros +=1
    return b8zs