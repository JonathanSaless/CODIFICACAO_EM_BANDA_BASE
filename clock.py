import numpy as np
import matplotlib.pyplot as plt
#CLOCK
def CLOCK(dados):
    dados_repetidos = np.repeat(dados, 2)
    clock = np.arange(1, 2*len(dados)+2) % 2   #cria lista com 0s e 1s
    plt.figure(figsize=(20, 2))
    plt.yticks(np.arange(0, 2))
    ax = plt.gca()                        
    ax.get_xaxis().set_visible(False)    #esconde eixo x
    for i in range(0, len(dados_repetidos), 2):
            plt.axvline(i, color="black", linestyle="--")
            plt.text(i+1, 1.1, dados_repetidos[i], ha = "center", va = "bottom")
    plt.axvline(len(dados_repetidos), color="black", linestyle="--")
        
    # Impressão em formato adequado à um clock digital
    plt.step(np.arange(len(clock)), clock, where='post', color="black")
    plt.show()